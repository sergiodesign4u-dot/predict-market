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


# =========================================================================
# SIGN IN / REGISTER
# =========================================================================
SI_FILES = {"form": "sign-in.html", "error": "sign-in-error.html",
            "loading": "sign-in-loading.html", "conflict": "sign-in-provider-conflict.html"}
SI_LABELS = [("form", "Form"), ("error", "Error"), ("loading", "Loading"), ("conflict", "Provider conflict")]

SI_PROVIDERS = """          <button type="button" class="provider-btn">
            <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8v8M8 12h8"/></svg>
            Continue with Google
          </button>
          <button type="button" class="provider-btn">
            <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 5l14 14M19 5L5 19"/></svg>
            Continue with X
          </button>
          <button type="button" class="provider-btn">
            <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 7c1-2 3-3 4-3 0 2-1 3-2 4M9 9c-2 0-4 2-4 5s2 6 4 6c1 0 1.5-.5 3-.5s2 .5 3 .5c1.5 0 3-2 3-4-2-1-2-4 0-5-1-1.5-3-1.5-4-1.5S11 9 9 9z"/></svg>
            Continue with Apple
          </button>"""

SI_TERMS = '          <p class="fine">No crypto wallet required. By continuing you agree to the <a href="#">Terms</a> and <a href="#">Privacy Policy</a>. Deposits via card require KYC; crypto-only accounts can connect a wallet instead.</p>'


def _link_providers(html, href):
    """Wrap each provider button in a link to the next flow step (idempotent)."""
    import re
    if 'class="provider-btn"><a' in html or '"><button type="button" class="provider-btn"' in html:
        return html
    return re.sub(r'(<button type="button" class="provider-btn">.*?</button>)',
                  r'<a href="%s">\1</a>' % href, html, flags=re.S)


def si_form():
    # On the reference page, a successful provider sign-in advances to Deposit (authOk -> DEP).
    body = ('          <p class="fine">You are about to place a bet. Sign in or create an account to continue. It takes a few seconds.</p>\n'
            + _link_providers(SI_PROVIDERS, "deposit.html") + "\n"
            + SI_TERMS)
    return overlay("Event Detail (Confirm in the bet panel)",
                   "zone: Sign In / Register (modal on desktop, bottom sheet on mobile; social login, FJ3)",
                   "Sign in or create account", body, "event-detail.html")


def si_loading():
    body = ('          <div class="spinner-box">Redirecting to Google to sign in...<br><span class="fine">Waiting for the provider. This window stays open.</span></div>\n'
            '          <button type="button" class="provider-btn" style="justify-content:center;">Cancel and choose another provider</button>')
    return overlay("Event Detail (Confirm in the bet panel)",
                   "zone: Sign In / Register (loading: OAuth redirect pending)",
                   "Signing you in", body, "event-detail.html")


def si_error():
    body = ('          <div class="inline-error">Sign-in failed. The provider did not complete authentication. You can try again or use a different provider.</div>\n'
            + SI_PROVIDERS + "\n"
            + SI_TERMS)
    return overlay("Event Detail (Confirm in the bet panel)",
                   "zone: Sign In / Register (error: auth failed, T5 - retry or use other provider)",
                   "Sign in or create account", body, "event-detail.html")


def si_conflict():
    body = ('          <div class="inline-error">This email is already registered with <strong>X</strong>. To keep one account, continue with X, or link Google to your existing account.</div>\n'
            '          <button type="button" class="provider-btn">\n'
            '            <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 5l14 14M19 5L5 19"/></svg>\n'
            '            Continue with X (your original provider)\n'
            '          </button>\n'
            '          <button type="button" class="provider-btn" style="justify-content:center;">Link Google to this account</button>\n'
            + SI_TERMS)
    return overlay("Event Detail (Confirm in the bet panel)",
                   "zone: Sign In / Register (provider-conflict: account exists under a different provider)",
                   "Account already exists", body, "event-detail.html")


SI_SIDE = """    <aside class="annotations" aria-label="Annotations">
      <span class="zone-tag">annotations: zone to job / finding</span>
      <ol>
        <li><strong>Social login (Google, X, Apple)</strong> -&gt; FJ3: bet with ordinary effort, no unfamiliar technology. News Junkie path, no crypto wallet required.</li>
        <li><strong>Modal / bottom sheet over a dimmed screen</strong> -&gt; invoked screen (conventions 5 + 7): the bet context behind stays visible, so the gate does not feel like leaving the flow.</li>
        <li><strong>error -&gt; retry or other provider</strong> -&gt; IA/flows.md T5 (auth error) recovery edge: T5 returns to Sign In.</li>
        <li><strong>provider-conflict</strong> -&gt; account exists under a different provider; resolve by using the original or linking, so the user is not locked out or duplicated.</li>
        <li><strong>Success leads to Deposit</strong> -&gt; on auth success the flow continues to Deposit (IA/flows.md authOk -&gt; DEP); there is no separate success page, the form is the base.</li>
      </ol>
    </aside>

    <div class="nav-col">
      <section class="navtree" aria-label="Navigation tree">
        <span class="zone-tag">on-page nav tree (main-flow spine)</span>
<pre>Main-flow spine (MJ, News Junkie):

Event Feed
   v
Event Detail   (bet panel; Confirm fires the gate)
   v
[Sign In / Register]   &lt;- current screen
   v
Deposit
   v
Active Bets</pre>
        <p class="ref">Flow position: MJ, News Junkie branch of the gate (IA/flows.md
          personaType -&gt; Sign In -&gt; authOk -&gt; Deposit). Serves FJ3.</p>
      </section>

      <section class="navtree" aria-label="States">
        <span class="zone-tag">states of this screen</span>
        <p class="ref">form (base / representative), loading (OAuth redirect pending),
          error (auth failed, T5 - retry or other provider), provider-conflict
          (account exists under another provider). Invoked overlay, no auth axis.</p>
      </section>
    </div>
"""

SI_AUTHSTATE = {"form": "state: form (provider selection)", "loading": "state: loading (OAuth in-progress)",
                "error": "state: error (auth failed, T5)", "conflict": "state: provider-conflict"}


def build_signin():
    out = []
    for st, fn in (("form", si_form), ("loading", si_loading), ("error", si_error), ("conflict", si_conflict)):
        out.append(page(SI_FILES[st], "Sign In / Register", SI_AUTHSTATE[st],
                        switcher(SI_FILES, SI_LABELS, st), fn(), SI_SIDE))
    return out


# =========================================================================
# DEPOSIT
# =========================================================================
DEP_FILES = {"form": "deposit.html", "loading": "deposit-loading.html", "error-card": "deposit-error-card.html",
             "error-kyc": "deposit-error-kyc.html", "widget-load-failure": "deposit-widget-load-failure.html",
             "pending": "deposit-pending.html", "minimum-not-met": "deposit-minimum-not-met.html"}
DEP_LABELS = [("form", "Form"), ("loading", "Loading"), ("error-card", "Card declined"),
              ("error-kyc", "KYC rejected"), ("widget-load-failure", "Widget failed"),
              ("pending", "Pending"), ("minimum-not-met", "Min not met")]

DEP_AMOUNT = """          <div>
            <span class="field-label">Amount to add</span>
            <div class="amount-row"><span class="amount-input">$20.00</span></div>
            <div class="quick">
              <button type="button">$10</button>
              <button type="button" class="sel">$20</button>
              <button type="button">$50</button>
              <button type="button">$100</button>
            </div>
          </div>"""

DEP_PROTECT = '          <p class="protect">Your USDC is held 1:1 - we do not lend or invest deposited funds.</p>'
DEP_FINE = '          <p class="fine">Minimum deposit $10. Card payments are converted to USDC via Transak. KYC is required for card deposits; crypto-only users can connect a USDC wallet instead.</p>'


def dep_form():
    body = (DEP_AMOUNT + "\n"
            '          <div>\n'
            '            <span class="field-label">Pay with</span>\n'
            '            <div class="widget-box">Transak payment widget (card to USDC)</div>\n'
            '          </div>\n'
            + DEP_PROTECT + "\n" + DEP_FINE + "\n"
            '          <a href="how-it-works.html"><button type="button" class="provider-btn" style="justify-content:center;width:100%;">How it works (what happens to my money)</button></a>\n'
            '          <a href="event-detail-bet-reconcile.html"><button type="button" class="confirm-btn" style="width:100%;">Add funds</button></a>')
    return overlay("Sign In / Register (just authenticated)",
                   "zone: Deposit (fiat card to USDC via Transak; funds-protection line, FJ4 / EJ2)",
                   "Add funds", body, "event-detail.html")


def dep_loading():
    body = ('          <div class="widget-box">Loading Transak...<br><span class="fine">KYC may be requested inside the widget. This can take a moment.</span></div>\n'
            '          <p class="fine">Do not close this window while the payment widget loads.</p>')
    return overlay("Sign In / Register (just authenticated)",
                   "zone: Deposit (loading: Transak widget loading / KYC pending inside the widget)",
                   "Add funds", body, "event-detail.html")


def dep_error_card():
    body = ('          <div class="inline-error">Your card was declined (T2). No funds were taken. Try another card, or connect a USDC wallet to skip cards entirely.</div>\n'
            + DEP_AMOUNT + "\n"
            '          <button type="button" class="confirm-btn">Try another card</button>\n'
            '          <button type="button" class="provider-btn" style="justify-content:center;">Connect a USDC wallet instead</button>')
    return overlay("Sign In / Register (just authenticated)",
                   "zone: Deposit (error-card: card declined, T2 - try another card or connect a wallet)",
                   "Card declined", body, "event-detail.html")


def dep_error_kyc():
    body = ('          <div class="inline-error">KYC verification was rejected (T1), so card deposits are not available on this account. You can still bet with crypto by connecting a USDC wallet (no KYC), or contact support.</div>\n'
            '          <button type="button" class="provider-btn" style="justify-content:center;">Connect a USDC wallet (no KYC)</button>\n'
            '          <button type="button" class="provider-btn" style="justify-content:center;">Contact support</button>\n'
            '          <a href="event-feed.html"><button type="button" class="provider-btn" style="justify-content:center;width:100%;">Back to feed</button></a>')
    return overlay("Sign In / Register (just authenticated)",
                   "zone: Deposit (error-KYC: KYC rejected, T1 - connect a USDC wallet or contact support)",
                   "Verification rejected", body, "event-detail.html")


def dep_widget_fail():
    body = ('          <div class="widget-box">Payment widget failed to load.<br><span class="fine">The Transak iframe was blocked or the network dropped.</span></div>\n'
            '          <button type="button" class="confirm-btn">Open Transak directly</button>\n'
            '          <button type="button" class="provider-btn" style="justify-content:center;">Connect a USDC wallet instead</button>\n'
            '          <p class="fine">Fallback per S3: route around the embedded widget when it cannot load.</p>')
    return overlay("Sign In / Register (just authenticated)",
                   "zone: Deposit (widget-load-failure: Transak iframe blocked - open directly or connect a wallet)",
                   "Payment didn't load", body, "event-detail.html")


def dep_pending():
    body = ('          <div class="spinner-box">Payment under review<br><span class="fine">This usually takes under 5 minutes. We will notify you when your funds are ready.</span></div>\n'
            '          <a href="event-detail.html"><button type="button" class="provider-btn" style="justify-content:center;width:100%;">Back to the event</button></a>\n'
            '          <a href="active-bets.html"><button type="button" class="provider-btn" style="justify-content:center;width:100%;">Go to My Bets</button></a>')
    return overlay("Sign In / Register (just authenticated)",
                   "zone: Deposit (pending: payment under review, usually under 5 min)",
                   "Payment pending", body, "event-detail.html")


def dep_min():
    body = ('          <div>\n'
            '            <span class="field-label">Amount to add</span>\n'
            '            <div class="amount-row"><span class="amount-input">$4.00</span></div>\n'
            '            <div class="inline-error">Minimum deposit is $10. Enter $10 or more to continue.</div>\n'
            '            <div class="quick">\n'
            '              <button type="button">$10</button>\n'
            '              <button type="button">$20</button>\n'
            '              <button type="button">$50</button>\n'
            '              <button type="button">$100</button>\n'
            '            </div>\n'
            '          </div>\n'
            + DEP_PROTECT + "\n"
            '          <button type="button" class="confirm-btn" aria-disabled="true">Add funds</button>')
    return overlay("Sign In / Register (just authenticated)",
                   "zone: Deposit (minimum-not-met: inline error before submit, shown against the amount)",
                   "Add funds", body, "event-detail.html")


DEP_SIDE = """    <aside class="annotations" aria-label="Annotations">
      <span class="zone-tag">annotations: zone to job / finding</span>
      <ol>
        <li><strong>Card to USDC via Transak</strong> -&gt; FJ3: ordinary money, no unfamiliar technology. Fiat on-ramp inside the platform.</li>
        <li><strong>Funds-protection line (held 1:1)</strong> -&gt; FJ4 + EJ2: a clear answer to "what happens to my money", shown before submit. Trust signal.</li>
        <li><strong>error-card (T2) / error-KYC (T1)</strong> -&gt; IA/flows.md recovery edges: a declined card offers another card or a wallet; a rejected KYC offers a no-KYC wallet path or support, never a dead end.</li>
        <li><strong>widget-load-failure</strong> -&gt; S3 fallback: open Transak directly or connect a wallet when the embedded widget is blocked.</li>
        <li><strong>pending / minimum-not-met</strong> -&gt; payment under review (with exits to the event or My Bets), and an inline minimum guard before submit.</li>
      </ol>
    </aside>

    <div class="nav-col">
      <section class="navtree" aria-label="Navigation tree">
        <span class="zone-tag">on-page nav tree (main-flow spine)</span>
<pre>Main-flow spine (MJ, News Junkie):

Event Feed
   v
Event Detail   (bet panel)
   v
Sign In / Register
   v
[Deposit]   &lt;- current screen
   v
Active Bets</pre>
        <p class="ref">Flow position: MJ, after Sign In on the News Junkie path
          (IA/flows.md authOk -&gt; Deposit -&gt; depOk -&gt; S5 reconcile). Serves FJ3, FJ4, EJ2.</p>
      </section>

      <section class="navtree" aria-label="States">
        <span class="zone-tag">states of this screen</span>
        <p class="ref">form (base), loading (widget / KYC in-progress), error-card (T2),
          error-KYC (T1), widget-load-failure (S3 fallback), pending (under review),
          minimum-not-met (inline). Invoked overlay, no auth axis.</p>
      </section>
    </div>
"""

DEP_AUTHSTATE = {"form": "state: form (amount + Transak)", "loading": "state: loading (widget in-progress)",
                 "error-card": "state: error-card (declined, T2)", "error-kyc": "state: error-KYC (rejected, T1)",
                 "widget-load-failure": "state: widget-load-failure (S3 fallback)",
                 "pending": "state: pending (under review)", "minimum-not-met": "state: minimum-not-met (inline)"}


def build_deposit():
    fns = {"form": dep_form, "loading": dep_loading, "error-card": dep_error_card, "error-kyc": dep_error_kyc,
           "widget-load-failure": dep_widget_fail, "pending": dep_pending, "minimum-not-met": dep_min}
    out = []
    for st in ("form", "loading", "error-card", "error-kyc", "widget-load-failure", "pending", "minimum-not-met"):
        out.append(page(DEP_FILES[st], "Deposit", DEP_AUTHSTATE[st],
                        switcher(DEP_FILES, DEP_LABELS, st), fns[st](), DEP_SIDE))
    return out


# =========================================================================
# BET SCREEN
# =========================================================================
BET_FILES = {"intent": "event-detail.html", "reconcile": "bet-screen-reconcile.html",
             "insufficient-balance": "bet-screen-insufficient-balance.html",
             "event-closed": "bet-screen-event-closed.html", "error": "bet-screen-error.html",
             "processing": "bet-screen-processing.html"}
BET_LABELS = [("intent", "Intent"), ("reconcile", "S5 reconcile"), ("insufficient-balance", "Insufficient balance"),
              ("event-closed", "Event closed"), ("error", "Error (on-chain)"), ("processing", "Processing")]

BET_DIR = """          <div>
            <span class="field-label">Your side</span><br>
            <span class="dir-pill">YES &middot; 38%</span>
            <button type="button" class="quick" style="border:none;background:none;padding:0;"><span style="text-decoration:underline;font-size:11px;">switch to NO</span></button>
          </div>
          <p class="fine" style="margin:0;">Will the US government shut down before March 1, 2027?</p>"""

BET_AMOUNT = """          <div>
            <span class="field-label">Amount</span>
            <div class="amount-row"><span class="amount-input">$5.00</span></div>
            <div class="quick">
              <button type="button" class="sel">$5</button>
              <button type="button">$10</button>
              <button type="button">$25</button>
              <button type="button">$50</button>
            </div>
          </div>"""


def bet_lines(balance="$42.00"):
    return f"""          <div>
            <div class="line"><span>Price now</span><span>38%</span></div>
            <div class="line"><span>Platform fee (earned only if you win)</span><span>$0.40</span></div>
            <div class="line total"><span>Potential payout</span><span>$13.20</span></div>
            <div class="line"><span>Your balance</span><span>{balance}</span></div>
          </div>"""

BET_FINE = '          <p class="fine">No minimum or maximum. Payout depends on when you bet: AMM pricing rewards earlier stakes. The platform earns its fee only if you win.</p>'


def bet_intent():
    body = (BET_DIR + "\n" + BET_AMOUNT + "\n" + bet_lines() + "\n" + BET_FINE + "\n"
            '          <button type="button" class="confirm-btn">Confirm bet</button>\n'
            '          <p class="fine" style="text-align:center;">Confirm fires the account gate (sign in, then deposit if needed).</p>')
    return overlay("Event Detail (YES tapped)",
                   "zone: Bet Screen - intent (logged out, user builds the bet; Confirm fires the gate)",
                   "Place your bet", body, "event-detail.html")


def bet_reconcile():
    body = (BET_DIR + "\n"
            '          <div class="reconcile-box">\n'
            '            <strong>The price moved while you signed in</strong>\n'
            '            <span>Was: YES 38% &nbsp;-&gt;&nbsp; Now: YES 41%</span>\n'
            '            <span class="fine">Your potential payout changed from $13.20 to $12.20 for the same $5 stake. Confirm the new price or cancel.</span>\n'
            '          </div>\n'
            + bet_lines() + "\n"
            '          <button type="button" class="confirm-btn">Confirm at new price (41%)</button>\n'
            '          <a href="event-detail.html"><button type="button" class="provider-btn" style="justify-content:center;width:100%;">Cancel and re-evaluate the event</button></a>')
    return overlay("Deposit (just completed) / wallet",
                   "zone: Bet Screen - S5 reconcile (price moved during the gate; re-confirm or T16 cancel)",
                   "Price updated", body, "event-detail.html")


def bet_insufficient():
    body = (BET_DIR + "\n"
            '          <div>\n'
            '            <span class="field-label">Amount</span>\n'
            '            <div class="amount-row"><span class="amount-input">$25.00</span></div>\n'
            '            <div class="inline-error">You have $3.00. You can bet up to $3.00, or add funds to bet more.</div>\n'
            '            <div class="quick"><button type="button">$1</button><button type="button">$3 (max)</button></div>\n'
            '          </div>\n'
            '          <a href="deposit.html"><button type="button" class="confirm-btn">Add funds</button></a>\n'
            '          <button type="button" class="provider-btn" style="justify-content:center;">Bet $3.00 instead</button>')
    return overlay("Event Detail (YES tapped)",
                   "zone: Bet Screen - insufficient-balance (inline: bet up to balance or deposit more)",
                   "Place your bet", body, "event-detail.html")


def bet_event_closed():
    body = ('          <div class="state-block" style="border:none;background:none;padding:6px 0;">\n'
            '            <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M15 9l-6 6M9 9l6 6"/></svg>\n'
            '            <h2 class="state-title">This event just closed</h2>\n'
            '            <p class="state-msg">The market resolved while you were placing your bet, so this bet cannot be completed. No funds were taken.</p>\n'
            '            <div class="state-actions">\n'
            '              <a href="event-feed.html"><button type="button" class="state-btn primary">Back to feed</button></a>\n'
            '              <a href="active-bets.html"><button type="button" class="state-btn">See your bets</button></a>\n'
            '            </div>\n'
            '          </div>')
    return overlay("Event Detail (now resolved)",
                   "zone: Bet Screen - event-closed (event resolved while on screen; no position to view here)",
                   "Event closed", body, "event-feed.html")


def bet_error():
    body = (BET_DIR + "\n"
            '          <div class="inline-error">Your bet did not register on-chain (T3). No funds were taken. You can try again, or check your wallet.</div>\n'
            + bet_lines() + "\n"
            '          <button type="button" class="confirm-btn">Try again</button>\n'
            '          <button type="button" class="provider-btn" style="justify-content:center;">Check wallet</button>')
    return overlay("Deposit (just completed) / wallet",
                   "zone: Bet Screen - error (bet registration failed on-chain, T3 - retry returns to execute)",
                   "Bet didn't go through", body, "event-detail.html")


def bet_processing():
    body = (BET_DIR + "\n"
            '          <div class="spinner-box">Registering your bet on-chain...<br><span class="fine">This usually takes a few seconds. Keep this window open.</span></div>\n'
            + bet_lines())
    return overlay("Deposit (just completed) / wallet",
                   "zone: Bet Screen - execute on-chain processing (transitional: to success / Active Bets or T3)",
                   "Placing your bet", body, "event-detail.html")


BET_SIDE = """    <aside class="annotations" aria-label="Annotations">
      <span class="zone-tag">annotations: zone to job / finding</span>
      <ol>
        <li><strong>Pre-set direction (YES) + $5 default amount</strong> -&gt; MJ + FJ3: the real stake with low friction; side comes from the card / Event Detail tap, amount is pre-filled and quick-selectable.</li>
        <li><strong>Fee and potential payout inline</strong> -&gt; transparency (design principle): "platform earns its fee only if you win"; payout depends on timing (AMM).</li>
        <li><strong>Confirm fires the gate</strong> -&gt; intent is logged out; Confirm routes to Sign In, then Deposit (IA/flows.md confirmedIntent -&gt; gate).</li>
        <li><strong>S5 reconcile</strong> -&gt; the AMM price can move during the gate; old vs new price is shown and the user re-confirms, or cancels (T16).</li>
        <li><strong>insufficient-balance / event-closed / error / processing</strong> -&gt; deposit more or bet to balance; closed market exits to feed / My Bets; on-chain failure (T3) retries; the processing state is the transitional execute moment.</li>
      </ol>
    </aside>

    <div class="nav-col">
      <section class="navtree" aria-label="Navigation tree">
        <span class="zone-tag">on-page nav tree (main-flow spine)</span>
<pre>Main-flow spine (MJ, News Junkie):

Event Feed
   v
Event Detail
   v
[Bet Screen]   &lt;- current screen
   v
Sign In / Register
   v
Deposit
   v
Active Bets</pre>
        <p class="ref">Flow position: MJ, after the YES/NO tap (IA/flows.md BS1 intent -&gt;
          gate -&gt; ... -&gt; S5 reconcile -&gt; BS2 execute -&gt; Active Bets). Serves MJ, FJ3.</p>
      </section>

      <section class="navtree" aria-label="States">
        <span class="zone-tag">states of this screen</span>
        <p class="ref">intent (base, logged out), S5-reconcile (price moved, re-confirm / T16),
          insufficient-balance (inline), event-closed (resolved while on screen),
          error (on-chain, T3 retry), execute processing (transitional). The base is intent,
          so there is no separate success page: success is the move to Active Bets. Invoked overlay.</p>
      </section>
    </div>
"""

BET_AUTHSTATE = {"intent": "state: intent (logged out, building the bet)", "reconcile": "state: S5-reconcile (price moved)",
                 "insufficient-balance": "state: insufficient-balance (inline)", "event-closed": "state: event-closed",
                 "error": "state: error (on-chain, T3)", "processing": "state: execute on-chain processing"}


def build_bet():
    fns = {"intent": bet_intent, "reconcile": bet_reconcile, "insufficient-balance": bet_insufficient,
           "event-closed": bet_event_closed, "error": bet_error, "processing": bet_processing}
    out = []
    for st in ("intent", "reconcile", "insufficient-balance", "event-closed", "error", "processing"):
        out.append(page(BET_FILES[st], "Bet Screen", BET_AUTHSTATE[st],
                        switcher(BET_FILES, BET_LABELS, st), fns[st](), BET_SIDE))
    return out


allf = build_signin() + build_deposit()
print("\n".join(allf))
