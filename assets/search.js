/* assets/search.js - the catalog, and the one behaviour that reads it.

   WHY THIS IS A FILE AND NOT 108 COPIES. Every other script in this tree is
   inline and per-screen, which is right for a thing that is ABOUT that screen:
   the sub-category rail reads the cards standing on the page it is in. Search
   is the opposite. It answers from every screen in the product about events
   that are on none of them - a person searching from `wallet.html` is asking
   about the feed - so the answer cannot be read out of the document it is asked
   in, and a copy of the catalog in each of 108 files is 108 places for the
   catalog to drift. It loads exactly the way `assets/icons.js` does, for the
   same measured reason: a script tag resolves from disk and from a server
   alike, where a fetch over `file://` has no origin to match.

   THE CATALOG IS EXTRACTED, NOT WRITTEN. Taken 2026-08-17 from the painted tree
   by walking every `<article class="card">` in `ui-visual/*.html` for its `.q`,
   its `data-cat`, its `data-subcat`, its lead figure and its volume, plus the
   one question that is only ever an `<h1 class="ed-q">`. 27 events, re-taken
   2026-08-20 when the first two recurring markets landed (`docs/backlog.md` 224);
   25 until then, the number `ia/docs/sitemap.md` cites for this catalog and the
   number that overturned the IA's deferral of search in the first place. If the tree grows
   an event and this file is not re-taken, search will not find it: that is the
   cost of a second copy and it is written here rather than discovered later.

   THE MARKUP IS SOMEWHERE ELSE. The sheet, its groups, the category tiles and
   the popular rows are static markup in each screen, because structure is the
   tree's and not a script's. What is here is the query: filter, render, count.
   The desktop panel is the one exception and it is a deliberate one, below. */
(function () {
  'use strict';

  var CATALOG = [
  {q:"Will Bitcoin close above $150,000 before October 1, 2026?",h:"event-detail.html",c:"Crypto",s:"Bitcoin",p:"61% YES"},
  {q:"Will Ethereum complete its next major network upgrade before November 1, 2026?",h:"event-detail.html",c:"Crypto",s:"Ethereum",p:"72% YES"},
  {q:"Which party will control the US Senate after the next election?",h:"event-detail-multi.html",c:"Politics",s:"Midterm Elections",p:"Republicans 52%"},
  {q:"Will the US government shut down before March 1, 2027?",h:"event-detail.html",c:"Politics",s:"Government Shutdown",p:"38% YES"},
  {q:"Will a spot Solana ETF be approved before September 1, 2027?",h:"event-detail.html",c:"Crypto",s:"ETFs",p:"44% YES"},
  {q:"Will Ethereum stay above $4,000 through the end of 2026?",h:"event-detail.html",c:"Crypto",s:"Ethereum",p:"54% YES"},
  {q:"Will Bitcoin close above $119,500 in the week to Jul 3?",h:"event-detail-recurring.html",c:"Crypto",s:"Bitcoin",p:"54% YES"},
  {q:"Will Ethereum close above $4,200 in the week to Jul 3?",h:"event-detail-recurring.html",c:"Crypto",s:"Ethereum",p:"47% YES"},
  {q:"Who will win the 2027 Eurovision final?",h:"event-detail-multi.html",c:"Culture",s:"Awards",p:"Sweden 34%"},
  {q:"Which party will win the most seats in the next UK general election?",h:"event-detail-multi.html",c:"Politics",s:"Global Elections",p:"Labour 44%"},
  {q:"Who will win the 2028 Republican presidential nomination?",h:"event-detail-multi.html",c:"Politics",s:"Nomination",p:"DeSantis 31%"},
  {q:"Will the next US federal budget pass before the October deadline?",h:"event-detail.html",c:"Politics",s:"Congress",p:"41% YES"},
  {q:"Which chain will hold the largest stablecoin supply at the end of July 2026?",h:"event-detail-recurring-multi.html",c:"Crypto",s:"Stablecoins",p:"Ethereum 58%"},
  {q:"Will a US spot XRP ETF be approved before June 1, 2027?",h:"event-detail.html",c:"Crypto",s:"ETFs",p:"31% YES"},
  {q:"Will the EU formally admit a new member state before January 1, 2028?",h:"event-detail.html",c:"Politics",s:"Europe",p:"23% YES"},
  {q:"Will a crewed mission return from lunar orbit before January 1, 2028?",h:"event-detail.html",c:"General",s:"Space",p:"39% YES"},
  {q:"Will a snap national election be called in France before July 1, 2027?",h:"event-detail.html",c:"Politics",s:"Global Elections",p:"29% YES"},
  {q:"Will 2026 be confirmed as one of the three warmest years on record before April 1, 2027?",h:"event-detail.html",c:"General",s:"Climate",p:"55% YES"},
  {q:"Will the top-grossing 2026 film pass $2 billion worldwide?",h:"event-detail.html",c:"Culture",s:"Movies",p:"22% YES"},
  {q:"Will a Category 5 hurricane form in the Atlantic during the 2026 season?",h:"event-detail.html",c:"General",s:"Climate",p:"62% YES"},
  {q:"Which genre will lead the 2026 summer box office?",h:"event-detail-multi.html",c:"Culture",s:"Movies",p:"Superhero 46%"},
  {q:"Which energy source will add the most new capacity in 2026?",h:"event-detail-multi.html",c:"General",s:"Business",p:"Solar 51%"},
  {q:"Will the next lead actor for the Bond film be announced before December 31, 2026?",h:"event-detail.html",c:"Culture",s:"Movies",p:"47% YES"},
  {q:"Will the next major game console launch before the 2026 holiday season?",h:"event-detail.html",c:"Culture",s:"Gaming",p:"58% YES"},
  {q:"Will a new monthly global temperature record be set in July 2026?",h:"event-detail-recurring.html",c:"General",s:"Climate",p:"48% YES"},
  {q:"Will global renewable capacity set a new annual record in 2026?",h:"event-detail.html",c:"General",s:"Climate",p:"74% YES"},
  {q:"Will a debut album top the 2026 year-end chart?",h:"event-detail.html",c:"Culture",s:"Music",p:"35% YES"}
  ];

  var RESULTS_PAGE = 'event-feed-search-results.html';
  var IN_SURFACE = 6;          /* rows the surface answers with before the seam */
  var RAIL = 900;              /* 56.25rem at the default root: components/search.css */

  function esc(s) { return s.replace(/[&<>"]/g, function (c) { return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c]; }); }

  /* THE MARK IS DRAWN ON THE ESCAPED STRING, never on the raw one, and the two
     have to be measured in the same coordinates: the index comes from the
     lower-cased ORIGINAL, so the slice is taken from the original too and each
     of the three pieces is escaped on its own. Escaping first and matching
     after would put the highlight in the wrong place the moment a question
     carries an `&`. */
  function mark(text, q) {
    if (!q) return esc(text);
    var i = text.toLowerCase().indexOf(q.toLowerCase());
    if (i < 0) return esc(text);
    return esc(text.slice(0, i)) + '<mark>' + esc(text.slice(i, i + q.length)) + '</mark>' + esc(text.slice(i + q.length));
  }

  function match(q) {
    var n = q.trim().toLowerCase();
    if (!n) return [];
    return CATALOG.filter(function (e) {
      return (e.q + ' ' + e.c + ' ' + e.s).toLowerCase().indexOf(n) > -1;
    });
  }

  function row(e, q) {
    return '<li><a class="nav-item nav-row nav-row-stack" href="' + e.h + '">' +
      '<strong>' + mark(e.q, q.trim()) + '</strong>' +
      '<span>' + esc(e.c) + (e.p ? ' &middot; ' + esc(e.p) : '') + '</span></a></li>';
  }

  /* ONE SURFACE = ONE BODY. `surface` is the sheet or the panel; everything
     below reads only from inside it, so the two never see each other's nodes
     and a screen that carries both keeps two independent answers. */
  function render(surface, q) {
    if (!surface) return;
    var typed = q.trim();
    var hits = match(typed);
    var idle = surface.querySelectorAll('[data-idle]');
    var res = surface.querySelector('[data-query]');
    var list = surface.querySelector('[data-results]');
    var none = surface.querySelector('[data-none]');
    var all = surface.querySelector('[data-seeall]');
    var i;

    for (i = 0; i < idle.length; i++) idle[i].hidden = !!typed;
    if (res) res.hidden = !typed || !hits.length;
    if (none) {
      none.hidden = !typed || !!hits.length;
      var b = none.querySelector('b');
      if (b) b.textContent = typed;
    }
    if (list) list.innerHTML = hits.slice(0, IN_SURFACE).map(function (e) { return row(e, typed); }).join('');
    if (all) {
      all.hidden = !typed || !hits.length;
      all.href = RESULTS_PAGE + '?q=' + encodeURIComponent(typed);
      var lab = all.querySelector('[data-seeall-label]');
      if (lab) lab.textContent = 'See all ' + hits.length + (hits.length === 1 ? ' result' : ' results');
    }
  }

  document.addEventListener('DOMContentLoaded', function () {
    var sheet = document.getElementById('searchSheet');
    var inline = document.querySelector('.search-inline');
    var panel = inline && inline.querySelector('.search-panel');

    /* THE PANEL IS A CLONE AND THAT IS THE POINT. The groups are written ONCE
       per screen, in the sheet, and the panel takes a copy of them the first
       time it opens. Written twice they would be two lists of five categories
       and four popular events in one file, and this repository has already
       measured what a second copy costs: the day one of them gains an event,
       the other is wrong and nothing says so. Nothing inside a group carries an
       `id` for exactly this reason - a clone of an `id` is a duplicate `id`,
       which the tree's own sweep counts. */
    function fill() {
      if (!panel || !sheet || panel.firstElementChild) return;
      var body = sheet.querySelector('.search-body');
      if (body) panel.appendChild(body.cloneNode(true));
    }

    function surfaceOf(el) { return el.closest('.search-sheet') || el.closest('.search-inline'); }

    function openSheet(e) {
      if (!sheet || !sheet.showModal) return;             /* no dialog, no script: the link stands */
      if (e) e.preventDefault();
      sheet.showModal();
      var f = sheet.querySelector('.search-input');
      if (f) { f.focus(); render(sheet, f.value); }
    }
    function closeSheet() { if (sheet && sheet.open) sheet.close(); }

    document.addEventListener('click', function (e) {
      var open = e.target.closest('.search-open');
      if (open) { openSheet(e); return; }
      if (e.target.closest('[data-close-search]')) { e.preventDefault(); closeSheet(); return; }
      if (panel && !panel.hidden && !inline.contains(e.target)) panel.hidden = true;
    });

    /* A `<dialog>` closed with Escape fires `close`, so the field is emptied
       there rather than in the handler above: the two ways out then leave the
       same state behind, which is the whole reason a cancel is not a second
       kind of close. */
    if (sheet) sheet.addEventListener('close', function () {
      var f = sheet.querySelector('.search-input');
      if (f) { f.value = ''; render(sheet, ''); }
    });

    document.addEventListener('input', function (e) {
      var f = e.target.closest('.search-input');
      if (!f) return;
      var s = surfaceOf(f);
      if (s === inline) { fill(); if (panel) panel.hidden = false; }
      render(s === inline ? panel : s, f.value);
    });

    document.addEventListener('focusin', function (e) {
      var f = e.target.closest('.search-input');
      if (!f || surfaceOf(f) !== inline) return;
      fill();
      if (panel) { panel.hidden = false; render(panel, f.value); }
    });

    document.addEventListener('keydown', function (e) {
      if (e.key !== 'Escape' || !panel || panel.hidden) return;
      panel.hidden = true;
      var f = inline.querySelector('.search-input');
      if (f) f.focus();
    });

    /* THE CLEAR CONTROL EMPTIES AND STAYS. `search.css` hides it while the
       field is empty, so the button removes itself the moment it works; the
       focus goes back to the field because a person who cleared a query is
       about to type another one. */
    document.addEventListener('click', function (e) {
      var c = e.target.closest('.search-clear');
      if (!c) return;
      e.preventDefault();
      var s = surfaceOf(c);
      var f = s && s.querySelector('.search-input');
      if (!f) return;
      f.value = '';
      render(s === inline ? panel : s, '');
      f.focus();
    });

    document.addEventListener('submit', function (e) {
      var form = e.target.closest('[data-search]');
      if (!form) return;
      var f = form.querySelector('.search-input');
      var v = f ? f.value.trim() : '';
      if (!v) { e.preventDefault(); return; }
      e.preventDefault();
      window.location.href = RESULTS_PAGE + '?q=' + encodeURIComponent(v);
    });

    /* A WINDOW DRAGGED PAST THE RUNG HAS TWO WAYS IN OPEN AT ONCE. The mark
       goes `display:none` at 900 and the field appears, and a sheet already
       open would sit over a header that now has its own field. The sheet is the
       one that goes, because the field is the answer at that width. */
    window.addEventListener('resize', function () {
      if (sheet && sheet.open && window.innerWidth >= RAIL) closeSheet();
    });

    /* The results page and the sheet both read `?q=`, so a link into either
       arrives with the query already in the field rather than with an empty
       box and a heading about a word nobody can see. */
    var q = new URLSearchParams(window.location.search).get('q');
    if (q) {
      var fields = document.querySelectorAll('.search-input');
      for (var i = 0; i < fields.length; i++) {
        fields[i].value = q;
        /* THE PAGE'S OWN FILTER LISTENS FOR `input` AND A SCRIPTED `.value =`
           DOES NOT FIRE ONE, so without this line the results page would arrive
           carrying the query in a box and the whole unfiltered grid under it:
           the field would say `election` and the count would say 24. The event
           is dispatched rather than the filter called, because that filter is
           the page's and this file does not know its name. */
        fields[i].dispatchEvent(new Event('input', { bubbles: true }));
      }
      if (sheet) render(sheet, q);
    }
  });

  window.YonderSearch = { catalog: CATALOG };
})();
