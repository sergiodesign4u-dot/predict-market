#!/usr/bin/env python3
"""_deposit_input.py - idempotent post-processor (Stage 08, UI+Visual).

Makes the Add-funds (deposit) dialog interactive, matching the bet panel, on
every ui-visual page that carries it (the shared chrome, ~76 pages). Voice-safe:
edits ONLY ui-visual/*.html, never wireframes/, never a gen_*.py regenerate.

Two changes per page:
  1. The amount field becomes a REAL input. `<span class="amount-input">$20.00</span>`
     -> `<input class="amount-input" type="text" inputmode="decimal" ...>` so the
     user can type their own number (digit-only, enforced by the JS below + the
     shared theme states that already exist for the dialog input).
  2. A guarded <script id="uv-deposit"> wires it: the quick chips ($10/$20/$50/$100)
     select + fill the input, typing your own number clears the chip, and the input
     stays numeric ($ + digits + one dot, no letters). This mirrors the kit's own
     generic amount/chip handlers so kit and pages behave identically.

Because event-feed.html is one of the pages processed here and the kit extracts its
deposit dialog from event-feed.html, rebuilding the kit after this run gives the kit
the real input too. Chip :hover / input :focus states live in the shared theme.

Idempotent (span already converted -> skip; script strip+reinject). Run:
    python3 ui-visual/_deposit_input.py   (then rebuild the kit)
"""
import re
import pathlib

HERE = pathlib.Path(__file__).resolve().parent

SPAN_RE = re.compile(r'<span class="amount-input">([^<]*)</span>')

def to_input(m):
    val = m.group(1).strip() or '$20.00'
    return ('<input class="amount-input" type="text" inputmode="decimal" '
            f'pattern="[0-9.$]*" value="{val}" aria-label="Amount to add">')

UV_DEPOSIT = '''  <script id="uv-deposit">
(function(){
  // Non-bet amount fields (the deposit dialog + the wallet withdraw form). Bet
  // panels/sheets keep their own richer handlers, so skip .bp-inner contexts.
  function betCtx(el){return el.closest('.bet-panel,.bet-sheet,.bp-inner');}
  // amount stays numeric ($ + digits + a single dot; no letters); typing your own
  // number clears any preset chip in the same group
  document.querySelectorAll('input.amount-input').forEach(function(inp){
    if(betCtx(inp))return;
    inp.addEventListener('input',function(){
      var dollar=inp.value.trim().charAt(0)==='$';
      var v=inp.value.replace(/[^0-9.]/g,''); var p=v.split('.'); if(p.length>2)v=p[0]+'.'+p.slice(1).join('');
      inp.value=(dollar?'$':'')+v;
      var box=inp.closest('.sheet-body,.app-dialog,form');
      if(box)box.querySelectorAll('.quick button').forEach(function(b){b.classList.remove('sel');});
    });
  });
  // quick chip: select it and fill the nearest amount input
  document.querySelectorAll('.quick').forEach(function(q){
    if(betCtx(q))return;
    q.addEventListener('click',function(e){
      var b=e.target.closest('button'); if(!b||!q.contains(b))return;
      q.querySelectorAll('button').forEach(function(x){x.classList.remove('sel');}); b.classList.add('sel');
      var box=q.closest('.sheet-body,.app-dialog,form,section')||document;
      var inp=box.querySelector('input.amount-input');
      if(inp){var v=b.textContent.replace(/[^0-9.]/g,'');var dollar=inp.value.trim().charAt(0)==='$';inp.value=(dollar?'$':'')+v+(dollar?'.00':'');}
    });
  });
})();
  </script>
'''

def strip_block(html, block_id):
    pat = re.compile(r'[ \t]*<script id="' + re.escape(block_id) + r'">.*?</script>\n?', re.S)
    return pat.sub('', html)

def process(path):
    html = path.read_text(encoding='utf-8')
    if 'id="depositDialog"' not in html:
        return False
    before = html
    # 1. span -> input (deposit is the only span.amount-input)
    html = SPAN_RE.sub(to_input, html)
    # 2. (re)inject the interactive script
    html = strip_block(html, 'uv-deposit')
    idx = html.rfind('</body>')
    if idx != -1:
        html = html[:idx] + UV_DEPOSIT + html[idx:]
    if html != before:
        path.write_text(html, encoding='utf-8')
        return True
    return False

def main():
    touched = [p.name for p in sorted(HERE.glob('*.html')) if process(p)]
    print(f"_deposit_input.py: updated {len(touched)} page(s)")
    if touched:
        print("  " + ", ".join(touched[:6]) + (f" ... (+{len(touched)-6} more)" if len(touched) > 6 else ""))

if __name__ == '__main__':
    main()
