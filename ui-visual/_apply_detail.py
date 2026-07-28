#!/usr/bin/env python3
"""
Apply the Vault colour layer to the whole Event Detail family (13 pages).

Mirror of _apply_theme.py's "shell + swap": ui-visual/event-feed.html is the
finished, themed shell (head links, roadmap sidebar, uv-bar, themed header /
bottom-nav / footer, dialogs, scripts). For every detail page we start from that
shell and:
  1. swap the shell's <main class="feed"> for the wireframe's detail <main>,
     normalised to one <div class="feed-inner"> with the category bar (Politics
     active) on top, so the content plates ride the same slab the feed uses;
  2. inject a thin Vault odds bar under the big YES/NO odds (binary pages only);
  3. rebuild Related events as thumbnail rows + a Load-more-style button;
  4. lift the mobile sticky bet-dock in just after </main> (inside .app-case),
     when the variant has one;
  5. for logged-out pages, also swap the header + mobile bottom-nav.

Grafted fragments come from wireframes/ (grey): product .html links -> "#". The
comment "like" hearts stay hearts (main); the Favorites heart in the swapped
CHROME becomes a bookmark (matches the themed header). The detail-only inline
LAYOUT CSS the feed shell lacks is grafted into <head>; _theme.css re-skins it.
State banners (resolved / error) use the already-themed .state-* rules.

Idempotent. NEVER edits wireframes/, NEVER regenerates event-feed.html.
Run:  python3 _apply_detail.py   then   python3 _resync_sidebar.py
"""
import re
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
UIV = ROOT / "ui-visual"
WF = ROOT / "wireframes"

SHELL = (UIV / "event-feed.html").read_text()

HEART = "M12 21s-7-4.5-9.5-9C1 9 2.6 5.5 6 5.5c2 0 3.2 1.3 4 2.4.8-1.1 2-2.4 4-2.4 3.4 0 5 3.5 3.5 6.5C19 16.5 12 21 12 21z"
BOOKMARK = "M6 3h12v18l-6-4-6 4z"

CAT_ACTIVE = "event-feed-politics.html"   # every sample detail event is Politics

# Concept-demo behaviour: YES/NO switch; a live editable amount input + quick
# chips that recompute Price now / Fee / Potential payout.
TOGGLE_JS = """<script>
(function(){
  /* YES/NO selector + dock: click switches the active item */
  document.querySelectorAll('.bp-dir, .bet-dock').forEach(function(group){
    var items = group.querySelectorAll('.bp-side');
    if(items.length < 2) return;
    items.forEach(function(btn){
      btn.addEventListener('click', function(){
        items.forEach(function(b){ b.classList.remove('sel'); });
        btn.classList.add('sel');
      });
    });
  });
  /* per bet panel: live amount, quick chips, recomputed fee/payout */
  document.querySelectorAll('.bet-panel').forEach(function(panel){
    var input = panel.querySelector('.amount-input');
    var dir = panel.querySelector('.bp-dir');
    var hint = panel.querySelector('.bp-hint');
    function num(v){ return parseFloat(String(v).replace(/[^0-9.]/g, '')) || 0; }
    function money(x){ return '$' + x.toFixed(2); }
    function sideBtn(){ return panel.querySelector('.bp-dir .bp-side.sel') || (dir && dir.querySelector('.bp-side')); }
    function setLine(prefix, val){
      panel.querySelectorAll('.line').forEach(function(line){
        var s = line.querySelectorAll('span');
        if(s.length >= 2 && s[0].textContent.indexOf(prefix) === 0){ s[s.length - 1].textContent = val; }
      });
    }
    function recompute(){
      if(!input) return;
      var A = num(input.value), btn = sideBtn();
      if(!btn) return;
      var pctEl = btn.querySelector('.bp-pct');
      var p = pctEl ? num(pctEl.textContent) / 100 : 0.5;
      var payout = p > 0 ? A / p : 0, fee = 0.03 * payout;
      setLine('Price now', Math.round(p * 100) + '%');
      setLine('Fee', money(fee));
      setLine('Potential payout', money(payout));
    }
    if(dir){
      dir.querySelectorAll('.bp-side').forEach(function(b){
        b.addEventListener('click', function(){
          if(hint){ hint.textContent = (b.textContent || '').trim().split(/\\s+/)[0] + ' selected'; }
          recompute();
        });
      });
    }
    panel.querySelectorAll('.quick button').forEach(function(chip){
      chip.addEventListener('click', function(){
        panel.querySelectorAll('.quick button').forEach(function(b){ b.classList.remove('sel'); });
        chip.classList.add('sel');
        if(input){ input.value = money(num(chip.textContent)); }
        recompute();
      });
    });
    if(input){
      input.addEventListener('input', function(){
        panel.querySelectorAll('.quick button').forEach(function(b){ b.classList.remove('sel'); });
        recompute();
      });
      input.addEventListener('blur', function(){ input.value = money(num(input.value)); recompute(); });
    }
    recompute();
  });
  /* price chart (single line): fill the polyline + X axis, switch on 1d/1w/1m/all */
  document.querySelectorAll('.ed-chart:not(.ed-chart-multi)').forEach(function(chart){
    var poly = chart.querySelector('.chart-svg polyline');
    var xaxis = chart.querySelector('.ed-xaxis');
    if(!poly) return;
    var DATA = {
      '1d':  {s:[40,41,39,42,40,43,41,42,40,38], x:['24h','18h','12h','6h','now']},
      '1w':  {s:[46,44,48,45,50,43,45,41,39,38], x:['7d','5d','3d','1d','now']},
      '1m':  {s:[44,46,42,45,41,47,43,48,45,50,46,52,49,44,38], x:['30d','3w','2w','1w','now']},
      'all': {s:[41,44,40,36,47,43,50,45,49,44,53,57,38], x:['Jul','Sep','Nov','Jan','now']}
    };
    function render(key){
      var d = DATA[key] || DATA.all, n = d.s.length;
      poly.setAttribute('points', d.s.map(function(v,i){ return (i/(n-1)*300).toFixed(1)+','+(100-v).toFixed(1); }).join(' '));
      if(xaxis){ xaxis.innerHTML = d.x.map(function(t){ return '<span>'+t+'</span>'; }).join(''); }
    }
    chart.querySelectorAll('.ed-range button').forEach(function(btn){
      btn.addEventListener('click', function(){
        chart.querySelectorAll('.ed-range button').forEach(function(b){ b.classList.remove('sel'); });
        btn.classList.add('sel');
        render(btn.textContent.trim().toLowerCase());
      });
    });
    var sel = chart.querySelector('.ed-range button.sel') || chart.querySelector('.ed-range button:last-child');
    render(sel ? sel.textContent.trim().toLowerCase() : 'all');
  });
  /* multi-outcome chart: ALL outcome lines + legend; range switch + highlight */
  document.querySelectorAll('.ed-chart-multi').forEach(function(chart){
    var NAMES=['JD Vance','Donald Trump','Ron DeSantis','Nikki Haley','Other'];
    var COLORS=['#4fd694','#5b9df0','#d9b968','#c77dff','#9aa0aa'];
    var DATA=[
      [38,40,37,41,39,43,40,44,42,47,44,49,41],
      [26,24,27,25,23,22,24,21,23,20,22,21,22],
      [16,17,15,16,14,15,13,14,13,15,14,13,14],
      [10,9,11,8,10,9,10,8,9,7,9,8,8],
      [10,10,10,10,14,11,13,13,13,11,11,9,15]
    ];
    var XL={'1d':['24h','18h','12h','6h','now'],'1w':['7d','5d','3d','1d','now'],'1m':['30d','3w','2w','1w','now'],'all':['Jul','Sep','Nov','Jan','now']};
    var NPTS={'1d':5,'1w':7,'1m':10,'all':13};
    var lines=chart.querySelectorAll('.ml-line');
    var xaxis=chart.querySelector('.ed-xaxis');
    var legend=chart.querySelector('.ed-legend');
    var nowEl=chart.querySelector('.ed-chart-now');
    var sel=0;
    function range(){ var b=chart.querySelector('.ed-range button.sel'); return b?b.textContent.trim().toLowerCase():'all'; }
    function draw(){
      var key=range(), n=NPTS[key]||13;
      lines.forEach(function(ln,i){
        var s=DATA[i].slice(-n);
        ln.setAttribute('points', s.map(function(v,j){ return (j/(s.length-1)*300).toFixed(1)+','+(100-v).toFixed(1); }).join(' '));
        ln.style.stroke=COLORS[i];
        ln.style.opacity=(i===sel)?'1':'0.28';
        ln.style.strokeWidth=(i===sel)?'2.2':'1.3';
      });
      if(xaxis){ xaxis.innerHTML=(XL[key]||XL.all).map(function(t){ return '<span>'+t+'</span>'; }).join(''); }
    }
    function legendHTML(){ if(legend){ legend.innerHTML=NAMES.map(function(nm,i){ return '<span class="lg-item'+(i===sel?' sel':'')+'"><i style="background:'+COLORS[i]+'"></i>'+nm+'</span>'; }).join(''); } }
    function nowHTML(){ if(nowEl){ nowEl.textContent=NAMES[sel]+' '+DATA[sel][DATA[sel].length-1]+'% now'; nowEl.style.color=COLORS[sel]; } }
    chart.selectOutcome=function(i){ sel=i; draw(); legendHTML(); nowHTML(); };
    chart.querySelectorAll('.ed-range button').forEach(function(b){ b.addEventListener('click',function(){ chart.querySelectorAll('.ed-range button').forEach(function(x){ x.classList.remove('sel'); }); b.classList.add('sel'); draw(); }); });
    draw(); legendHTML(); nowHTML();
  });
  /* multi outcomes list: click an outcome to select it (fill + tag + sync bet panel + chart) */
  document.querySelectorAll('#edOutcomes').forEach(function(box){
    var rows=box.querySelectorAll('.opt-row');
    var chart=document.querySelector('.ed-chart-multi');
    rows.forEach(function(row,i){
      row.addEventListener('click',function(){
        rows.forEach(function(r){ r.classList.remove('sel'); var t=r.querySelector('.opt-sel-tag'); if(t) t.remove(); });
        row.classList.add('sel');
        var nameEl=row.querySelector('.opt-name');
        var nm=nameEl.childNodes[0].textContent.trim();
        var prob=row.querySelector('.opt-prob').textContent;
        var tag=document.createElement('span'); tag.className='opt-sel-tag'; tag.textContent='selected';
        nameEl.appendChild(document.createTextNode(' ')); nameEl.appendChild(tag);
        var bp=document.querySelector('.bp-selected .bp-sel-name');
        if(bp){ bp.innerHTML=nm+' <span class="opt-prob">'+prob+'</span>'; }
        if(chart && chart.selectOutcome){ chart.selectOutcome(i); }
      });
    });
  });
  /* Rules / Market Context tabs */
  document.querySelectorAll('.ed-rules').forEach(function(box){
    var tabs = box.querySelectorAll('.rules-tab'), panels = box.querySelectorAll('.rules-panel');
    tabs.forEach(function(tab, i){
      tab.addEventListener('click', function(){
        tabs.forEach(function(t){ t.classList.remove('sel'); });
        tab.classList.add('sel');
        panels.forEach(function(p, j){ p.hidden = (j !== i); });
      });
    });
  });
  /* header actions: save-into-Favorites toggle + jump to comments */
  document.querySelectorAll('.ed-actions [data-fav]').forEach(function(b){
    b.addEventListener('click', function(){
      b.setAttribute('aria-pressed', b.getAttribute('aria-pressed') === 'true' ? 'false' : 'true');
    });
  });
  document.querySelectorAll('.ed-actions [data-comments]').forEach(function(b){
    b.addEventListener('click', function(){
      var r = document.getElementById('edtab-comments'); if(r){ r.checked = true; }
      var t = document.querySelector('.ed-tabs'); if(t){ t.scrollIntoView({behavior:'smooth', block:'start'}); }
    });
  });
})();
</script>
"""

# (slug, wireframe, logged_out, title suffix). slug "" -> event-detail.html.
STATES = [
    ("",                   "event-detail.html",                    False, "binary"),
    ("multi",              "event-detail-multi.html",              False, "multi-outcome"),
    ("resolved",           "event-detail-resolved.html",           False, "resolved"),
    ("loading",            "event-detail-loading.html",            False, "loading"),
    ("error",              "event-detail-error.html",              False, "error"),
    ("bet-reconcile",      "event-detail-bet-reconcile.html",      False, "bet: price moved"),
    ("bet-insufficient",   "event-detail-bet-insufficient.html",   False, "bet: low balance"),
    ("bet-processing",     "event-detail-bet-processing.html",     False, "bet: processing"),
    ("bet-error",          "event-detail-bet-error.html",          False, "bet: error"),
    ("logged-out",         "event-detail-logged-out.html",         True,  "logged out"),
    ("logged-out-multi",   "event-detail-logged-out-multi.html",   True,  "logged out, multi"),
    ("logged-out-loading", "event-detail-logged-out-loading.html", True,  "logged out, loading"),
    ("logged-out-error",   "event-detail-logged-out-error.html",   True,  "logged out, error"),
]


def block(html, open_marker, close_tag):
    """Return (start, end, substring) from open_marker through close_tag inclusive."""
    s = html.index(open_marker)
    e = html.index(close_tag, s) + len(close_tag)
    return s, e, html[s:e]


def swap(html, open_marker, close_tag, new):
    s, e, _ = block(html, open_marker, close_tag)
    return html[:s] + new + html[e:]


def neutralize(frag):
    """Main fragment: product links dead; comment like-hearts KEPT as hearts."""
    return re.sub(r'href="[^"]*\.html[^"]*"', 'href="#"', frag)


def neutralize_chrome(frag):
    """Header / bottom-nav fragment: links dead + Favorites heart -> bookmark,
    so the logged-out chrome matches the themed logged-in header."""
    return neutralize(frag).replace(HEART, BOOKMARK)


# The category bar (grabbed once), Politics active, real category hrefs kept live.
_, _, _SHELL_CATNAV = block(SHELL, '<nav class="cat-nav"', "</nav>")
CATNAV = (_SHELL_CATNAV.replace(' aria-current="page"', '')
          .replace(f'<li><a href="{CAT_ACTIVE}">',
                   f'<li aria-current="page"><a href="{CAT_ACTIVE}">', 1))


def first_style(html):
    s = html.index("<style>")
    e = html.index("</style>", s)
    return s, e, html[s + len("<style>"):e]


SHELL_STYLE_LINES = {ln.strip() for ln in first_style(SHELL)[2].splitlines()}


def graft_detail_css(out, wf):
    """Graft the detail-only inline LAYOUT CSS (tab switching, hidden radios,
    flex rows, chart sizing, panel/dock breakpoints, bet-state boxes) the feed
    shell's <style> lacks in before </style>; _theme.css re-skins the colour."""
    detail_css = first_style(wf)[2]
    extra = [ln for ln in detail_css.splitlines()
             if ln.strip() and ln.strip() not in SHELL_STYLE_LINES]
    graft = ("\n    /* ---- Event Detail layout, grafted from the wireframe; "
             "_theme.css re-skins colour ---- */\n" + "\n".join(extra) + "\n  ")
    _, e, _ = first_style(out)
    return out[:e] + graft + out[e:]


def strip_feed_inner(inner):
    """Remove a wireframe's own <div class="feed-inner"> wrapper (only the resolved
    page has one) by balanced <div> matching, so every variant re-wraps uniformly."""
    tag = '<div class="feed-inner">'
    i = inner.find(tag)
    if i < 0:
        return inner
    j = i + len(tag)
    depth = 1
    for m in re.finditer(r'<div\b|</div>', inner[j:]):
        if m.group() == "</div>":
            depth -= 1
            if depth == 0:
                cs, ce = j + m.start(), j + m.end()
                return inner[:i] + inner[j:cs] + inner[ce:]
        else:
            depth += 1
    return inner


def _balanced_div(frag, open_marker):
    """(start, end, html) of a full <div ...>...</div> block by balanced matching."""
    i = frag.find(open_marker)
    if i < 0:
        return None
    j = frag.index(">", i) + 1
    depth = 1
    for m in re.finditer(r"<div\b|</div>", frag[j:]):
        if m.group() == "</div>":
            depth -= 1
            if depth == 0:
                end = j + m.end()
                return (i, end, frag[i:end])
        else:
            depth += 1
    return None


def resolved_to_side(frag):
    """Resolved page: move the 'This event just resolved' banner OUT of the full-width
    top block INTO the right column (like the bet panel), so the left column shows the
    event and the right shows the resolved state. No-op unless it's the resolved page."""
    if "This event just resolved" not in frag:
        return frag
    sb = _balanced_div(frag, '<div class="state-block"')
    if not sb:
        return frag
    banner = sb[2]
    frag = frag[:sb[0]] + frag[sb[1]:]
    em = _balanced_div(frag, '<div class="ed-main"')
    if not em:
        return frag
    panel = '<aside class="bet-panel resolved-panel"><div class="rp-inner">' + banner + "</div></aside>"
    layout = '<div class="ed-layout">' + em[2] + panel + "</div>"
    return frag[:em[0]] + layout + frag[em[1]:]


def wrap_state_plate(inner):
    """Pure-state pages (error) drop a raw .state-block straight into feed-inner, so
    it renders as its own bordered box. The feed's error/empty states instead ride the
    shared .cat-layout stone plate (state-block goes borderless via _theme.css). Wrap
    the detail state-block the same way, so it matches event-feed-*-error. The loading
    skeleton already rides the .ed-main plate, so skip anything with an ed-main."""
    if 'class="ed-main"' in inner or 'class="ed-layout"' in inner:
        return inner
    sb = _balanced_div(inner, '<div class="state-block"')
    if not sb:
        return inner
    block_html = sb[2].replace(' style="margin:8px;"', '')
    plate = ('<div class="cat-layout">\n        <div class="cat-main">\n        '
             + block_html + '\n        </div><!-- /cat-main --></div><!-- /cat-layout -->')
    return inner[:sb[0]] + plate + inner[sb[1]:]


def inject_action_sprites(out):
    """Insert the two Solar-Bold action symbols (chat + share) into the sprite <defs>,
    so #i-chat-b / #i-share-b resolve on detail pages. Idempotent; base file untouched."""
    if 'id="i-chat-b"' in out:
        return out
    return out.replace("</defs>", ACTION_SPRITES + "</defs>", 1)


def inject_oddsbar(frag):
    """Thin green-over-red Vault odds bar under .ed-prob-big (binary pages only),
    sized from YES%. No-op when there is no single YES/NO line (multi, states)."""
    m = re.search(r'<p class="ed-prob-big">.*?<span class="prob">(\d+)%</span>', frag, flags=re.S)
    if not m:
        return frag
    bar = ('\n                <div class="ed-oddsbar" aria-hidden="true">'
           f'<span class="track"><span class="fill" style="width:{m.group(1)}%"></span></span></div>')
    return re.sub(r'(<p class="ed-prob-big">.*?</p>)', lambda mm: mm.group(1) + bar,
                  frag, count=1, flags=re.S)


def setup_multi_chart(frag):
    """Multi page: turn the single-line chart into a multi-line one - 5 (empty)
    polylines the JS fills per outcome, plus a legend slot. No-op on non-multi."""
    if 'id="edOutcomes"' not in frag:
        return frag
    polys = "".join('<polyline class="ml-line" points=""/>' for _ in range(5))
    frag = frag.replace('<polyline points=""/>', polys, 1)
    frag = frag.replace('<section class="ed-section ed-chart">',
                        '<section class="ed-section ed-chart ed-chart-multi">', 1)
    frag = frag.replace('<div class="ed-chart-foot">',
                        '<div class="ed-legend" aria-hidden="true"></div><div class="ed-chart-foot">', 1)
    return frag


def reorder_multi(frag):
    """Multi page: move the Price chart ABOVE the Outcomes list (chart first)."""
    if 'id="edOutcomes"' not in frag:
        return frag
    om = re.search(r'<section class="ed-section" id="edOutcomes">.*?</section>', frag, flags=re.S)
    cm = re.search(r'<section class="ed-section ed-chart[^"]*">.*?</section>', frag, flags=re.S)
    if not om or not cm or cm.start() < om.start():
        return frag
    chart_html = cm.group(0)
    frag = frag[:cm.start()] + frag[cm.end():]
    om2 = re.search(r'<section class="ed-section" id="edOutcomes">', frag)
    return frag[:om2.start()] + chart_html + "\n          " + frag[om2.start():]


def thumb_for(q):
    ql = q.lower()
    if any(k in ql for k in ("bitcoin", "ethereum", "solana", "xrp", "stablecoin", "crypto", "chain", "etf")):
        return "../assets/event-crypto.jpg"
    if any(k in ql for k in ("party", "election", "senate", "government", "shutdown", "budget", "eu ", "france", "minister")):
        return "../assets/event-politics.jpg"
    if any(k in ql for k in ("eurovision", "bond", "album", "box office", "console", "game", "film", "genre")):
        return "../assets/spare-reader.jpg"
    return "../assets/spare-markets-dark.jpg"


def restyle_related(frag):
    """Rebuild Related events as thumbnail rows + lift the last plain link
    ("Browse more events", the row with no odds) into a Load-more-style button."""
    m = re.search(r'<section class="related-events".*?</section>', frag, flags=re.S)
    if not m:
        return frag
    sec = m.group(0)
    items, more = [], None
    for href, row in re.findall(r'<li><a href="([^"]*)">(.*?)</a></li>', sec, flags=re.S):
        om = re.search(r'<span class="rel-odds">.*?</span>', row, flags=re.S)
        if om:
            q = row[:om.start()].strip()
            items.append(
                f'          <li><a href="{href}">'
                f'<span class="rel-thumb" style="background-image:url({thumb_for(q)})"></span>'
                f'<span class="rel-q">{q}</span>{om.group(0)}</a></li>'
            )
        else:
            more = (href, row.strip())
    lis = "\n".join(items)
    more_btn = f'\n        <a href="{more[0]}" class="related-more">{more[1]}</a>' if more else ""
    rebuilt = ('<section class="related-events" aria-label="Related events">\n'
               '        <h2>Related events</h2>\n'
               '        <ul class="related-list">\n' + lis + '\n        </ul>' + more_btn
               + '\n      </section>')
    return frag[:m.start()] + rebuilt + frag[m.end():]


def restyle_chart(frag):
    """Rebuild the price-chart section as a proper graph: a % Y-axis, a plot with
    gridlines + an (empty) polyline the JS fills, a time X-axis the JS fills, the
    current value in the header, and a working range switcher (1d/1w/1m/all) under
    the chart. No-op on pages without a real price chart."""
    m = re.search(r'<section class="ed-section">\s*<h3>Price chart</h3>(.*?)</section>', frag, flags=re.S)
    if not m:
        return frag
    cap = re.search(r'<p class="chart-cap">(.*?)</p>', m.group(1), flags=re.S)
    if not cap:
        return frag
    spans = re.findall(r'<span[^>]*>(.*?)</span>', cap.group(1), flags=re.S)
    rng = spans[1] if len(spans) > 1 else "1d &middot; 1w &middot; 1m &middot; all"
    now = spans[2] if len(spans) > 2 else ""
    opts = [o.strip() for o in re.split(r'\s*(?:&middot;|·)\s*', rng) if o.strip()]
    buttons = "".join(
        '<button type="button"%s>%s</button>' % (' class="sel"' if o.lower() == "all" else "", o)
        for o in opts
    )
    grid = "".join('<line class="grid-l" x1="0" y1="%d" x2="300" y2="%d"/>' % (y, y) for y in (25, 50, 75))
    svg = ('<svg class="chart-svg" viewBox="0 0 300 100" preserveAspectRatio="none" aria-hidden="true">'
           + grid + '<polyline points=""/><line class="nowline" x1="300" y1="0" x2="300" y2="100"/></svg>')
    new_section = (
        '<section class="ed-section ed-chart">\n'
        f'            <div class="ed-chart-head"><h3>Price chart</h3><span class="ed-chart-now">{now}</span></div>\n'
        '            <div class="ed-chart-area">\n'
        '              <div class="ed-yaxis"><span>100%</span><span>75%</span><span>50%</span><span>25%</span><span>0%</span></div>\n'
        f'              <div class="ed-plot">{svg}</div>\n'
        '            </div>\n'
        '            <div class="ed-xaxis" aria-hidden="true"></div>\n'
        f'            <div class="ed-chart-foot"><div class="ed-range" role="group" aria-label="Time range">{buttons}</div></div>\n'
        '          </section>'
    )
    return frag[:m.start()] + new_section + frag[m.end():]


def restyle_betpanel(frag):
    """Polymarket-style amount block: the "Amount" label + balance sit on the LEFT,
    the big bet value is right-aligned, quick chips below it. Keeps our clarity
    breakdown (fee / potential payout) - just lifts "Your balance" up under Amount.
    No trader chrome (Buy/Sell/order type) - the product speaks to a spectator."""
    if 'class="bet-panel"' not in frag:
        return frag
    bal = re.search(r'<div class="line"><span>Your balance</span><span>([^<]*)</span></div>', frag)
    if bal:
        cashval = bal.group(1)
    else:                                  # insufficient-balance state has no line - use "You have $X"
        low = re.search(r'You have (\$\d[\d.,]*\d)', frag)
        # reconcile / processing / on-chain-error carry no balance figure either;
        # fall back to the same $42.00 every other logged-in bet panel states, so the
        # cash line is consistent across all placing-a-bet states.
        cashval = low.group(1) if low else "$42.00"
    cash = f'<span class="bp-cash">{cashval} cash</span>' if cashval else ""
    frag = re.sub(
        r'<span class="field-label">Amount</span>\s*<div class="amount-row"><span class="amount-input">([^<]*)</span></div>',
        lambda m: ('<div class="bp-amount-row"><div class="bp-amount-lbl">'
                   f'<span class="field-label">Amount</span>{cash}</div>'
                   f'<input class="amount-input" type="text" inputmode="decimal" '
                   f'value="{m.group(1)}" aria-label="Bet amount"></div>'),
        frag, count=1)
    if bal:
        frag = re.sub(r'\s*<div class="line"><span>Your balance</span><span>[^<]*</span></div>', '', frag, count=1)
    return frag


# The chrome icon system is a filled "Solar Bold" sprite (#i-bookmark-b, #i-bell-b).
# The head actions must speak the SAME language, so they reference sprites too: the
# Favorites action reuses the exact #i-bookmark-b from the header/cards, and we add
# two matching Solar-Bold symbols (chat + share) into the detail pages' sprite defs.
_FAV_ICON = '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><use href="#i-bookmark-b"/></svg>'
_SHARE_ICON = '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><use href="#i-share-b"/></svg>'
_CMT_ICON = '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><use href="#i-chat-b"/></svg>'

# Solar-Bold symbols (same family as #i-bookmark-b / #i-bell-b) injected into the sprite
# <defs> of every detail page, so #i-chat-b / #i-share-b / #i-heart-b resolve. The heart
# replaces the crooked hand-drawn outline heart on the comment likes. Base untouched.
ACTION_SPRITES = (
    '<symbol id="i-chat-b" viewBox="0 0 24 24"><path fill="currentColor" fill-rule="evenodd"'
    ' clip-rule="evenodd" d="M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2S2 6.477 2 12c0 1.6.376 3.112'
    ' 1.043 4.453c.178.356.237.763.134 1.148l-.595 2.226a1.3 1.3 0 0 0 1.591 1.592l2.226-.596a1.63'
    ' 1.63 0 0 1 1.149.133A9.96 9.96 0 0 0 12 22"/></symbol>'
    '<symbol id="i-share-b" viewBox="0 0 24 24"><path fill="currentColor" d="M13.803 5.333c0-1.84 1.507-3.333'
    ' 3.365-3.333c1.86 0 3.366 1.492 3.366 3.333c0 1.841-1.507 3.334-3.366 3.334a3.38 3.38 0 0 1-2.037-.678l-4.67'
    ' 3.204a3.3 3.3 0 0 1 0 1.62l4.67 3.204a3.38 3.38 0 0 1 2.037-.677c1.86 0 3.366 1.492 3.366 3.333S19.028 22'
    ' 17.168 22c-1.858 0-3.365-1.492-3.365-3.333q0-.413.098-.804l-4.67-3.204a3.38 3.38 0 0 1-2.037.677C5.507'
    ' 15.336 4 13.843 4 12.002s1.507-3.333 3.365-3.333c.762 0 1.474.252 2.037.677l4.67-3.204a3.3 3.3 0 0'
    ' 1-.099-.809"/></symbol>'
    '<symbol id="i-heart-b" viewBox="0 0 24 24"><path fill="currentColor" d="M2 9.137C2 14 6.02 16.591 8.962'
    ' 18.911C10 19.729 11 20.5 12 20.5s2-.77 3.038-1.59C17.981 16.592 22 14 22 9.138s-5.5-8.406-10-3.985C7.5.735'
    ' 2 4.275 2 9.137"/></symbol>'
)

# The crooked hand-drawn outline heart on the comment likes -> the clean filled Solar-Bold
# heart sprite, so the comment likes match the rest of the icon system.
_CMT_HEART_OLD = ('<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-7-4.5-9.5-9C1 9'
                  ' 2.6 5.5 6 5.5c2 0 3.2 1.3 4 2.4.8-1.1 2-2.4 4-2.4 3.4 0 5 3.5 3.5 6.5C19 16.5 12 21 12 21z"/></svg>')
_CMT_HEART_NEW = '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><use href="#i-heart-b"/></svg>'


def restyle_comment_likes(frag):
    """Swap the outline comment-like heart for the filled Solar-Bold heart sprite."""
    return frag.replace(_CMT_HEART_OLD, _CMT_HEART_NEW)
ED_ACTIONS = (
    '<div class="ed-actions">'
    f'<button type="button" class="ed-act" data-comments aria-label="Jump to comments">{_CMT_ICON}</button>'
    f'<button type="button" class="ed-act" aria-label="Share this event">{_SHARE_ICON}</button>'
    f'<button type="button" class="ed-act" data-fav aria-pressed="false" aria-label="Save into Favorites">{_FAV_ICON}</button>'
    '</div>'
)


def add_head_actions(frag):
    """Add the header action cluster (comments / share / save-into-Favorites) to the
    event head, and drop the now-redundant 'Save to Favorites' fact. Real content
    heads only (skips the loading skeleton, which has no .ed-q)."""
    if 'class="ed-q"' not in frag:
        return frag
    frag = frag.replace('<div class="ed-head">', '<div class="ed-head">' + ED_ACTIONS, 1)
    frag = re.sub(r'\s*<span>Save<b>to Favorites</b></span>', '', frag, count=1)
    return frag


MARKET_PANEL = (
    '<section class="ed-section ed-market">\n'
    '            <details class="market-box" open>\n'
    '              <summary class="market-head"><span class="market-title">Market'
    ' <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/>'
    '<path d="M12 11v5M12 8h.01"/></svg></span>'
    '<svg class="market-chevron" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg></summary>\n'
    '              <div class="market-body">\n'
    '                <div class="market-stats">'
    '<div><span class="ms-label">Yes price</span><span class="ms-val ms-yes">38%</span></div>'
    '<div><span class="ms-label">No price</span><span class="ms-val ms-no">62%</span></div>'
    '<div><span class="ms-label">24h</span><span class="ms-val ms-up">+2 pts</span></div>'
    '<div><span class="ms-label">Volume</span><span class="ms-val">$84,200</span></div>'
    '<div><span class="ms-label">Liquidity</span><span class="ms-val">$31,500</span></div>'
    '</div>\n'
    '                <div class="market-depth">'
    '<span class="md-title">Price by bet size</span>'
    '<span class="md-sub">How the YES price moves as your bet grows. This market runs on an AMM, not an order book.</span>'
    '<div class="md-table">'
    '<div class="md-row md-row-head"><span>Bet</span><span>Avg YES price</span><span>You receive if YES</span></div>'
    '<div class="md-row"><span class="md-bar" style="width:12%"></span><span class="md-amt">$10</span><span class="md-price">38%</span><span class="md-get">$26.32</span></div>'
    '<div class="md-row"><span class="md-bar" style="width:30%"></span><span class="md-amt">$100</span><span class="md-price">39%</span><span class="md-get">$256.41</span></div>'
    '<div class="md-row"><span class="md-bar" style="width:58%"></span><span class="md-amt">$1,000</span><span class="md-price">42%</span><span class="md-get">$2,380.95</span></div>'
    '<div class="md-row"><span class="md-bar" style="width:88%"></span><span class="md-amt">$5,000</span><span class="md-price">49%</span><span class="md-get">$10,204.08</span></div>'
    '</div></div>\n'
    '              </div>\n'
    '            </details>\n'
    '          </section>'
)


def add_market_panel(frag):
    """Insert an AMM-honest 'Market' panel (current state + price-by-bet-size depth)
    right after the facts strip. This is the AMM analog of Polymarket's order book,
    without pretending to be a CLOB. No-op on pages without a facts strip."""
    m = re.search(r'<div class="ed-facts">.*?</div>', frag, flags=re.S)
    if not m:
        return frag
    return frag[:m.end()] + "\n          " + MARKET_PANEL + frag[m.end():]


def add_rules_tabs(frag):
    """Consolidate the 'Why this price' + 'Resolution conditions' sections into one
    Polymarket-style tabbed block: Rules (how it resolves) + Market Context (the
    plain-language background). No-op if either section is missing."""
    why = re.search(r'<section class="ed-section">\s*<h3>Why this price</h3>(.*?)</section>', frag, flags=re.S)
    res = re.search(r'<section class="ed-section">\s*<h3>Resolution conditions</h3>(.*?)</section>', frag, flags=re.S)
    if not why or not res:
        return frag
    context_inner = why.group(1).strip()
    rules_inner = res.group(1).strip()
    note = ('<p class="rules-note">Background from the Predict Market team to explain '
            'the odds. It plays no role in how this market resolves.</p>')
    block = (
        '<section class="ed-section ed-rules">\n'
        '            <div class="rules-tabs" role="tablist">'
        '<button type="button" class="rules-tab sel">Rules</button>'
        '<button type="button" class="rules-tab">Market Context</button></div>\n'
        f'            <div class="rules-panel">{rules_inner}</div>\n'
        f'            <div class="rules-panel" hidden>{context_inner}{note}</div>\n'
        '          </section>'
    )
    frag = frag[:why.start()] + block + frag[why.end():]
    frag = re.sub(r'\s*<section class="ed-section">\s*<h3>Resolution conditions</h3>.*?</section>',
                  '', frag, count=1, flags=re.S)
    return frag


def build(slug, wf_name, logged_out, title_suffix):
    wf = (WF / wf_name).read_text()

    # ---- main: normalise to one feed-inner with the category bar on top ----
    _, _, wf_main = block(wf, '<main class="feed">', "</main>")
    inner = wf_main[len('<main class="feed">'):-len("</main>")]
    inner = strip_feed_inner(inner)
    inner = neutralize(inner).replace(' style="background:#e0e0e0;"', '')  # drop light skeleton fills
    inner = wrap_state_plate(resolved_to_side(restyle_betpanel(reorder_multi(setup_multi_chart(restyle_chart(
        restyle_related(restyle_comment_likes(inject_oddsbar(add_market_panel(add_head_actions(add_rules_tabs(inner)))))))))))
        )
    new_main = ('<main class="feed">\n      <div class="feed-inner">\n        '
                + CATNAV + inner + '</div><!-- /feed-inner -->\n    </main>')
    out = swap(SHELL, '<main class="feed">', "</main>", new_main)

    # ---- mobile bet dock, if this variant has one ----
    try:
        _, _, wf_dock = block(wf, '<div class="bet-dock"', "</div>")
        out = out.replace("</main>", "</main>\n      " + neutralize(wf_dock), 1)
    except ValueError:
        pass

    # ---- logged-out: swap the header + mobile bottom-nav ----
    if logged_out:
        _, _, wf_header = block(wf, '<header class="app-header">', "</header>")
        out = swap(out, '<header class="app-header">', "</header>", neutralize_chrome(wf_header))
        _, _, wf_nav = block(wf, '<nav class="bottom-nav"', "</nav>")
        out = swap(out, '<nav class="bottom-nav"', "</nav>", neutralize_chrome(wf_nav))

    # ---- grafted detail layout CSS + the two Solar-Bold action sprites ----
    out = graft_detail_css(out, wf)
    out = inject_action_sprites(out)

    # ---- title + uv-bar provenance ----
    out = re.sub(r"<title>.*?</title>",
                 f"<title>UI Visual - Event Detail ({title_suffix})</title>",
                 out, count=1, flags=re.S)
    out = out.replace("Color copy of wireframes/event-feed.html",
                      f"Color copy of wireframes/{wf_name}", 1)

    # concept-demo YES/NO toggle behaviour
    out = out.replace("</body>", TOGGLE_JS + "</body>", 1)

    dest = UIV / (f"event-detail-{slug}.html" if slug else "event-detail.html")
    dest.write_text(out)
    return dest.name


if __name__ == "__main__":
    for st in STATES:
        print("built", build(*st))
