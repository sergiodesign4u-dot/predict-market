#!/usr/bin/env python3
"""_bet_drawer.py - idempotent post-processor (Stage 08, UI+Visual).

Propagates three things from the UI kit to the shipped Event Detail pages, all
voice-safe (edits ONLY ui-visual/event-detail*.html; never wireframes/, never a
gen_*.py regenerate):

  1. The Polymarket-style mobile bet DRAWER. The sticky dock's YES / NO / Confirm
     stop being dead/gate buttons and instead slide up a bottom sheet (<dialog
     class="bet-sheet">) carrying the full form - side toggle, amount (digit-only),
     quick chips, live fee/payout, Confirm. Confirm preserves the signin gate.
     Applied to the 4 pages that carry a dock (binary + multi, in + logged-out).
     event-detail-resolved has no dock (trading closed) -> skipped.

  2. Multi-outcome left -> right SYNC: picking an outcome row on the left now also
     fills the desktop bet panel's YES/NO side (solid) and its percentages, matching
     the kit. Additive to the existing name + chart sync. Fires only where #edOutcomes
     exists (the multi pages).

  3. Digit-only AMOUNT inputs (no letters). Bound to input.amount-input (the deposit
     dialog's amount is a display <span>, so it is untouched). Applied to all 8 pages
     that carry a typed bet amount - the 4 dock pages (inside the drawer script) and
     the 4 bet-state pages (a minimal script).

Idempotent: every injection is guarded by a marker. Run:
    python3 ui-visual/_bet_drawer.py
"""
import re
import pathlib

HERE = pathlib.Path(__file__).resolve().parent

DOCK_PAGES = [
    "event-detail.html",
    "event-detail-multi.html",
    "event-detail-logged-out.html",
    "event-detail-logged-out-multi.html",
]
# bet-flow states: a typed amount input but no dock -> digit-only only
STATE_PAGES = [
    "event-detail-bet-processing.html",
    "event-detail-bet-error.html",
    "event-detail-bet-reconcile.html",
    "event-detail-bet-insufficient.html",
]

# ---- sheet templates -------------------------------------------------------

BINARY_SHEET = '''
      <dialog class="app-case app-dialog bet-sheet" id="betSheet" aria-label="Place your bet">
        <button type="button" class="sheet-grab" data-close-sheet aria-label="Close"></button>
        <div class="bp-inner">
          <div class="bp-head"><h3>Place your bet</h3><span class="bp-hint">YES selected</span></div>
          <div class="bp-dir"><button type="button" class="bp-side sel">YES <span class="bp-pct">38%</span></button><button type="button" class="bp-side">NO <span class="bp-pct">62%</span></button></div>
          <div>
            <div class="bp-amount-row"><div class="bp-amount-lbl"><span class="field-label">Amount</span><span class="bp-cash">$42.00 cash</span></div><input class="amount-input" type="text" inputmode="decimal" pattern="[0-9.$]*" value="$5.00" aria-label="Bet amount"></div>
            <div class="quick"><button type="button" class="sel">$5</button><button type="button">$10</button><button type="button">$25</button><button type="button">$50</button></div>
          </div>
          <div>
            <div class="line"><span>Price now</span><span>38%</span></div>
            <div class="line"><span>Fee (only if you win)</span><span>$0.20</span></div>
            <div class="line total"><span>Potential payout</span><span>$13.20</span></div>
          </div>
          <button type="button" class="confirm-btn" data-sheet-confirm style="width:100%">Confirm bet</button>
          <p class="fine">No minimum or maximum. Payout depends on when you bet (AMM).</p>
        </div>
      </dialog>
'''

MULTI_SHEET = '''
      <dialog class="app-case app-dialog bet-sheet" id="betSheet" aria-label="Place your bet">
        <button type="button" class="sheet-grab" data-close-sheet aria-label="Close"></button>
        <div class="bp-inner">
          <div class="bp-head"><h3>Place your bet</h3><span class="bp-hint">YES selected</span></div>
          <span class="field-label">Your outcome</span>
          <div class="bp-selected"><span class="bp-sel-name">JD Vance <span class="opt-prob">41%</span></span><a href="#edOutcomes" class="bp-change" data-close-sheet>Change</a></div>
          <div class="bp-dir"><button type="button" class="bp-side sel">YES <span class="bp-pct">41%</span></button><button type="button" class="bp-side">NO <span class="bp-pct">59%</span></button></div>
          <div>
            <div class="bp-amount-row"><div class="bp-amount-lbl"><span class="field-label">Amount</span><span class="bp-cash">$42.00 cash</span></div><input class="amount-input" type="text" inputmode="decimal" pattern="[0-9.$]*" value="$5.00" aria-label="Bet amount"></div>
            <div class="quick"><button type="button" class="sel">$5</button><button type="button">$10</button><button type="button">$25</button><button type="button">$50</button></div>
          </div>
          <div>
            <div class="line"><span>Price now</span><span>41%</span></div>
            <div class="line"><span>Fee (only if you win)</span><span>$0.40</span></div>
            <div class="line total"><span>Potential payout</span><span>$12.20</span></div>
          </div>
          <button type="button" class="confirm-btn" data-sheet-confirm style="width:100%">Confirm bet</button>
          <p class="fine">No minimum or maximum. Payout depends on when you bet (AMM).</p>
        </div>
      </dialog>
'''

# ---- drawer script (dock pages) -------------------------------------------
# digit-only amount inputs + the bottom-sheet wiring + multi left->right sync.

DRAWER_JS = '''  <script id="uv-drawer">
(function(){
  // digit-only: bet amount takes numbers, a dot and $ only (no letters)
  document.querySelectorAll('input.amount-input').forEach(function(inp){
    inp.addEventListener('input',function(){
      var caret=inp.selectionStart, cleaned=inp.value.replace(/[^0-9.$]/g,'');
      if(cleaned!==inp.value){inp.value=cleaned;try{inp.setSelectionRange(caret-1,caret-1);}catch(e){}}
    });
  });

  // multi: kit-style outcome selection. Clicking a row - or its YES / NO - selects
  // that outcome AND that side on the LEFT (the compact button fills solid, others
  // clear), then drives the desktop bet panel: outcome name, YES/NO side (solid),
  // percentages, and the panel's own recompute (dispatched click).
  var outBox=document.getElementById('edOutcomes');
  var deskPanel=document.querySelector('.ed-layout .bet-panel')||document.querySelector('.bet-panel');
  if(outBox){
    outBox.addEventListener('click',function(e){
      var row=e.target.closest('.opt-row'); if(!row||!outBox.contains(row))return;
      var btn=e.target.closest('.yesno.compact button');
      outBox.querySelectorAll('.opt-row').forEach(function(r){
        r.classList.remove('sel');
        r.querySelectorAll('.yesno.compact button').forEach(function(b){b.classList.remove('sel');});
      });
      row.classList.add('sel');
      var yn=row.querySelector('.yesno.compact'); if(!yn)return;
      var first=yn.querySelector('button:first-child');
      var chosen=btn||first; if(chosen)chosen.classList.add('sel');
      var isYes=(chosen===first);
      if(!deskPanel)return;
      var pe=row.querySelector('.opt-prob'), pct=pe?parseInt(pe.textContent,10):null;
      var ne=row.querySelector('.opt-name'), nm=ne?(ne.childNodes[0].textContent||'').trim():'';
      var selName=deskPanel.querySelector('.bp-sel-name');
      if(selName)selName.innerHTML=nm+' <span class="opt-prob">'+(pct!=null?pct+'%':'')+'</span>';
      var dir=deskPanel.querySelector('.bp-dir'); if(!dir)return;
      var yesBtn=dir.querySelector('.bp-side:first-child'), noBtn=dir.querySelector('.bp-side:last-child');
      var yp=yesBtn&&yesBtn.querySelector('.bp-pct'), np=noBtn&&noBtn.querySelector('.bp-pct');
      if(pct!=null){ if(yp)yp.textContent=pct+'%'; if(np)np.textContent=(100-pct)+'%'; }
      dir.querySelectorAll('.bp-side').forEach(function(x){x.classList.remove('sel');});
      var deskSide=isYes?yesBtn:noBtn;
      if(deskSide){deskSide.classList.add('sel'); deskSide.dispatchEvent(new MouseEvent('click',{bubbles:true}));}
    });
  }

  // mobile bottom sheet
  var sheet=document.getElementById('betSheet');
  if(!sheet)return;
  function num(v){return parseFloat(String(v).replace(/[^0-9.]/g,''))||0;}
  function money(x){return '$'+x.toFixed(2);}
  function side(){return sheet.querySelector('.bp-dir .bp-side.sel')||sheet.querySelector('.bp-dir .bp-side');}
  function recompute(){
    var inp=sheet.querySelector('.amount-input'); if(!inp)return;
    var A=num(inp.value), b=side(); if(!b)return;
    var pe=b.querySelector('.bp-pct'), p=pe?num(pe.textContent)/100:0.5;
    var payout=p>0?A/p:0, fee=0.03*payout;
    sheet.querySelectorAll('.line').forEach(function(l){
      var s=l.querySelectorAll('span'); if(s.length<2)return;
      var t=s[0].textContent;
      if(t.indexOf('Price now')===0)s[s.length-1].textContent=Math.round(p*100)+'%';
      else if(t.indexOf('Fee')===0)s[s.length-1].textContent=money(fee);
      else if(t.indexOf('Potential payout')===0)s[s.length-1].textContent=money(payout);
    });
  }
  sheet.querySelectorAll('.bp-dir .bp-side').forEach(function(b){
    b.addEventListener('click',function(){
      sheet.querySelectorAll('.bp-dir .bp-side').forEach(function(x){x.classList.remove('sel');});
      b.classList.add('sel');
      var h=sheet.querySelector('.bp-hint'); if(h)h.textContent=(b.textContent||'').trim().split(/\\s+/)[0]+' selected';
      recompute();
    });
  });
  sheet.querySelectorAll('.quick button').forEach(function(c){
    c.addEventListener('click',function(){
      sheet.querySelectorAll('.quick button').forEach(function(x){x.classList.remove('sel');});
      c.classList.add('sel');
      var inp=sheet.querySelector('.amount-input'); if(inp)inp.value=money(num(c.textContent));
      recompute();
    });
  });
  var sinp=sheet.querySelector('.amount-input');
  if(sinp){
    sinp.addEventListener('input',function(){sheet.querySelectorAll('.quick button').forEach(function(x){x.classList.remove('sel');});recompute();});
    sinp.addEventListener('blur',function(){sinp.value=money(num(sinp.value));recompute();});
  }
  function preselect(s){
    if(!s)return; var d=sheet.querySelector('.bp-dir'); if(!d)return;
    d.querySelectorAll('.bp-side').forEach(function(x){x.classList.remove('sel');});
    (s==='no'?d.querySelector('.bp-side:last-child'):d.querySelector('.bp-side:first-child')).classList.add('sel');
    var h=sheet.querySelector('.bp-hint'); if(h)h.textContent=(s==='no'?'NO':'YES')+' selected';
    recompute();
  }
  document.querySelectorAll('[data-open-sheet]').forEach(function(b){
    b.addEventListener('click',function(){
      preselect(b.getAttribute('data-open-sheet'));
      if(sheet.showModal)sheet.showModal();else sheet.setAttribute('open','');
    });
  });
  function closeSheet(){ if(sheet.close)sheet.close(); else sheet.removeAttribute('open'); }
  sheet.addEventListener('click',function(e){if(e.target===sheet)closeSheet();});
  sheet.querySelectorAll('[data-close-sheet]').forEach(function(c){c.addEventListener('click',function(e){e.preventDefault();closeSheet();});});
  var cf=sheet.querySelector('[data-sheet-confirm]');
  if(cf)cf.addEventListener('click',function(){
    closeSheet();
    var s=document.getElementById('signinDialog');
    if(s){if(s.showModal)s.showModal();else s.setAttribute('open','');}
  });
  recompute();
})();
  </script>
'''

# ---- minimal digit-only script (bet-state pages) --------------------------

NUMERIC_JS = '''  <script id="uv-numeric">
(function(){
  document.querySelectorAll('input.amount-input').forEach(function(inp){
    inp.addEventListener('input',function(){
      var caret=inp.selectionStart, cleaned=inp.value.replace(/[^0-9.$]/g,'');
      if(cleaned!==inp.value){inp.value=cleaned;try{inp.setSelectionRange(caret-1,caret-1);}catch(e){}}
    });
  });
})();
  </script>
'''


def strip_block(html, block_id):
    """Remove a previously-injected <script id="..."> block so it can be
    re-injected fresh on re-run (keeps the drawer JS updatable)."""
    pat = re.compile(r'[ \t]*<script id="' + re.escape(block_id) + r'">.*?</script>\n?', re.S)
    return pat.sub('', html)


def rewrite_dock(html):
    """Canonical dock: just the two YES / NO buttons, each opening the bottom sheet
    with that side preselected. The '$X to win' meta and the dock Confirm button are
    removed - the drawer already carries the stake, breakdown and Confirm, so a
    Confirm in the dock (no bet formed yet) only confuses. Scoped to the .bet-dock
    block so the desktop panel's identical buttons are untouched. Idempotent."""
    start = html.find('<div class="bet-dock"')
    if start == -1:
        return html, False
    end = html.find('</div>', start)
    if end == -1:
        return html, False
    dock = html[start:end]
    orig = dock
    if 'data-open-sheet' not in dock:
        dock = dock.replace('class="bp-side sel">', 'class="bp-side sel" data-open-sheet="yes">', 1)
        dock = dock.replace('class="bp-side">', 'class="bp-side" data-open-sheet="no">', 1)
    # drop the '$X to win' meta and the dock Confirm button (the drawer has them)
    dock = re.sub(r'\s*<span class="dock-meta">.*?</span>', '', dock, flags=re.S)
    dock = re.sub(r'\s*<button[^>]*class="confirm-btn"[^>]*>.*?</button>', '', dock, flags=re.S)
    if dock == orig:
        return html, False
    return html[:start] + dock + html[end:], True


def process_dock_page(path):
    html = path.read_text(encoding='utf-8')
    changed = False

    # 1. dock -> data-open-sheet
    html, dock_done = rewrite_dock(html)
    changed = changed or dock_done

    # 2. inject the sheet after the dock (before </div><!-- /app-case -->)
    if 'id="betSheet"' not in html:
        sheet = MULTI_SHEET if 'multi' in path.name else BINARY_SHEET
        marker = '</div><!-- /app-case -->'
        idx = html.find(marker)
        if idx != -1:
            html = html[:idx] + sheet + '    ' + html[idx:]
            changed = True

    # 3. (re)inject the drawer script before </body> - strip any prior copy first
    #     so the logic refreshes on re-run
    before = html
    html = strip_block(html, 'uv-drawer')
    idx = html.rfind('</body>')
    if idx != -1:
        html = html[:idx] + DRAWER_JS + html[idx:]
    if html != before:
        changed = True

    if changed:
        path.write_text(html, encoding='utf-8')
    return changed


def process_state_page(path):
    html = path.read_text(encoding='utf-8')
    if 'id="uv-numeric"' in html or 'id="uv-drawer"' in html:
        return False
    idx = html.rfind('</body>')
    if idx == -1:
        return False
    html = html[:idx] + NUMERIC_JS + html[idx:]
    path.write_text(html, encoding='utf-8')
    return True


def main():
    touched = []
    for name in DOCK_PAGES:
        p = HERE / name
        if p.exists() and process_dock_page(p):
            touched.append(name)
    for name in STATE_PAGES:
        p = HERE / name
        if p.exists() and process_state_page(p):
            touched.append(name)
    print(f"_bet_drawer.py: updated {len(touched)} page(s)")
    for t in touched:
        print(f"  - {t}")


if __name__ == '__main__':
    main()
