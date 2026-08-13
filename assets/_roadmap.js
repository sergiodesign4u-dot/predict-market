/* assets/_roadmap.js - the ONE registry of the course roadmap, and the only copy of it.

   WHAT IT REPLACES. The same outline stood as hand-written markup in 28 documents across five
   folders: `research/`, `user-research/`, `ia/` (including `ia/annotations/`), `voice/` and
   `concept/`. 785 lines of it. Turning one planned row into a link on 2026-08-11 was one edit
   repeated 27 times at two path depths, and the 28th file did not need that edit and needed a
   bigger one: `concept/concept.html` stopped at UI + Visual and had stood four rows behind since
   stage 09 shipped. NOTHING NOTICED, BECAUSE A SIDEBAR THAT ENDS EARLY LOOKS LIKE A SIDEBAR, and
   no page declared how long the list was supposed to be. docs/backlog.md 117.

   IT IS THE KIT'S ANSWER, ONE FOLDER OVER. `ui-kit/_nav.js` has held the stand's route since
   2026-08-07 for the same reason and under the same rules, and three of them are taken verbatim:

   1. THE ACTIVE ROW IS COMPUTED FROM THE PATH, never declared. A page cannot carry a stale copy
      of its own name, because the name IS the page. `ui-kit/_nav.js` records what a declared
      `KIT_ACTIVE` cost in the repository it came from.
   2. A ROW WITH NO PAGE IS VISIBLE, as a `<span class="planned">`. Hiding Animation and Handoff
      would make the roadmap look finished and lie about it.
   3. NO CSS OF ITS OWN. Every class written below is `components/course-chrome.css`, which all 28
      pages already link.

   AND ONE THING THAT IS NOT THE KIT'S. The stand's pages are siblings, so its registry holds bare
   file names. These 28 sit at two depths, so every path here is written from the REPOSITORY ROOT
   and the prefix is computed from this script's own `src` at load. A page therefore declares
   neither its name nor its depth, which are the two things a hand-copied panel gets wrong.

   WHAT A PAGE STILL DECLARES, and why it is not drift: its own section anchors, in an
   `<div class="sidebar-sub" data-roadmap-sub>` inside the empty `<aside>`. Those are headings of
   that document and belong to it. The registry never holds them. `ia/annotations/*` is the one
   exception and it runs the other way: its sub list is fourteen SIBLING pages, so it is route and
   it is here.

   THE OUTLINE COLLAPSES, which is why this is a tree and not a list. A stage you are not inside
   is one row. A stage you are inside opens, and it opens in one of three shapes that the markup
   had already settled and nobody had written down:
     - `group`  the stage label becomes a divider and its pages become rows (User Research)
     - `nested` the same, with the pages in named groups of their own (Information Architecture,
                whose own label divider stays quiet and whose Basic / Detailed divider lights)
     - `sub`    the stage stays a link and its pages become sub-links (Wireframe Annotations)

   No em dash in this file. */

window.COURSE_ROADMAP = [
  { label: 'Foundation Research', page: 'research/research.html', dir: 'research/' },
  {
    label: 'User Research', page: 'user-research/personas.html', dir: 'user-research/', open: 'group',
    items: [
      { label: 'Personas',   page: 'user-research/personas.html' },
      { label: 'JTBD',       page: 'user-research/jtbd.html' },
      { label: 'CJM As-Is',  page: 'user-research/cjm-as-is.html' },
      { label: 'CJM To-Be',  page: 'user-research/cjm-to-be.html' }
    ]
  },
  {
    /* The only stage with two layers, and the reason is 03a and 03b: the basic layer is the map a
       person can read and the detailed layer is the one a builder can build from. The stage label
       renders as a QUIET divider here and the layer divider is the one that lights, which is what
       the 6 hand-written copies did and none of them said why. */
    label: 'Information Architecture', page: 'ia/flows.html', dir: 'ia/', open: 'nested',
    groups: [
      { label: 'Basic layer', items: [
        { label: 'Flows',       page: 'ia/flows.html' },
        { label: 'Concept map', page: 'ia/concept-map.html' }
      ] },
      { label: 'Detailed layer', items: [
        { label: 'Overview',     page: 'ia/ia.html' },
        { label: 'Sitemap',      page: 'ia/sitemap.html' },
        { label: 'SEO layer',    page: 'ia/seo.html' },
        { label: 'System nodes', page: 'ia/system.html' }
      ] }
    ]
  },
  { divider: 'Plan' },
  { label: 'Wireframes', page: 'wireframes/event-feed.html' },
  {
    label: 'Wireframe Annotations', page: 'ia/annotations/index.html', dir: 'ia/annotations/', open: 'sub',
    items: [
      { label: 'Event Feed',     page: 'ia/annotations/event-feed.html' },
      { label: 'Event Detail',   page: 'ia/annotations/event-detail.html' },
      { label: 'Category Pages', page: 'ia/annotations/category.html' },
      { label: 'My Bets',        page: 'ia/annotations/active-bets.html' },
      { label: 'Favorites',      page: 'ia/annotations/favorites.html' },
      { label: 'Deposit',        page: 'ia/annotations/deposit.html' },
      { label: 'Sign In',        page: 'ia/annotations/sign-in.html' },
      { label: 'My Profile',     page: 'ia/annotations/my-profile.html' },
      { label: 'Public Profile', page: 'ia/annotations/public-profile.html' },
      { label: 'Wallet',         page: 'ia/annotations/wallet.html' },
      { label: 'Notifications',  page: 'ia/annotations/notifications.html' },
      { label: 'How It Works',   page: 'ia/annotations/how-it-works.html' },
      { label: 'Win Screen',     page: 'ia/annotations/win.html' },
      { label: 'Loss Screen',    page: 'ia/annotations/loss.html' }
    ]
  },
  { label: 'Voice', page: 'voice/voice.html', dir: 'voice/' },
  { divider: 'Design and Delivery' },
  { label: 'Concept',       page: 'concept/concept.html', dir: 'concept/' },
  { label: 'UI + Visual',   page: 'ui-visual/event-feed.html' },
  { label: 'Design System', page: 'ui-kit/overview.html' },
  { label: 'Responsive',    page: 'ui-kit/responsive.html' },
  { label: 'Animation', planned: true },
  { label: 'Handoff',   planned: true }
];

(function () {
  /* The prefix is this file's own location, which is the only thing on the page that knows how
     deep the page is. `document.currentScript` is read at parse time on purpose: it is null by
     the time DOMContentLoaded fires. */
  var self = document.currentScript && document.currentScript.src;
  var ROOT = self ? self.replace(/assets\/_roadmap\.js.*$/, '') : '/';
  var here = location.pathname.replace(/\/index\.html$/, '/index.html');

  function isHere(page) {
    return here === '/' + page || here.slice(-(page.length + 1)) === '/' + page;
  }
  function inside(dir) {
    return dir ? here.indexOf('/' + dir) !== -1 : false;
  }
  function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;'); }

  function link(item, cls) {
    var on = isHere(item.page) ? ' active' : '';
    return '<a class="' + cls + on + '" href="' + ROOT + item.page + '">' + esc(item.label) + '</a>' +
           (on ? '<!--SUB-->' : '');
  }

  /* The active stage is the DEEPEST directory that matches, because `ia/annotations/` lives
     inside `ia/` and is its own stage. A shortest-match rule would open Information Architecture
     on all fifteen annotation pages, which is the one thing the hand-written copies got right and
     a naive registry gets wrong. */
  function activeStage(list) {
    var best = null, bestLen = 0;
    list.forEach(function (s) {
      if (s.dir && inside(s.dir) && s.dir.length > bestLen) { best = s; bestLen = s.dir.length; }
      else if (!s.dir && s.page && isHere(s.page) && bestLen === 0) { best = s; }
    });
    return best;
  }

  function render() {
    var host = document.getElementById('sidebar');
    if (!host || !window.COURSE_ROADMAP) return;
    var sub = host.querySelector('[data-roadmap-sub]');
    var subHTML = sub ? sub.outerHTML.replace(' data-roadmap-sub="" hidden', '').replace(' data-roadmap-sub', '').replace(' hidden', '') : '';
    var list = window.COURSE_ROADMAP;
    var stage = activeStage(list);
    var h = '';

    /* Which divider lights is a property of the ACTIVE stage's position in the list, not of the
       divider: the one above the active stage, and only if the stage does not raise a divider of
       its own. */
    var lit = null;
    if (stage) {
      var last = null;
      for (var i = 0; i < list.length; i++) {
        if (list[i].divider) last = list[i];
        if (list[i] === stage) { lit = (stage.open === 'group' || stage.open === 'nested') ? null : last; break; }
      }
    }

    list.forEach(function (s) {
      if (s.divider) {
        h += '<div class="sidebar-divider' + (s === lit ? ' active' : '') + '">' + esc(s.divider) + '</div>';
        return;
      }
      if (s.planned) {
        h += '<span class="sidebar-page-link planned">' + esc(s.label) + '</span>';
        return;
      }
      if (s !== stage) {
        h += '<a class="sidebar-page-link" href="' + ROOT + s.page + '">' + esc(s.label) + '</a>';
        return;
      }
      if (s.open === 'group') {
        h += '<div class="sidebar-divider active">' + esc(s.label) + '</div>';
        s.items.forEach(function (i) { h += link(i, 'sidebar-page-link'); });
      } else if (s.open === 'nested') {
        h += '<div class="sidebar-divider">' + esc(s.label) + '</div>';
        s.groups.forEach(function (g) {
          var on = g.items.some(function (i) { return isHere(i.page); });
          h += '<div class="sidebar-divider' + (on ? ' active' : '') + '">' + esc(g.label) + '</div>';
          g.items.forEach(function (i) { h += link(i, 'sidebar-page-link'); });
        });
      } else if (s.open === 'sub') {
        h += '<a class="sidebar-page-link active" href="' + ROOT + s.page + '">' + esc(s.label) + '</a>';
        h += '<div class="sidebar-sub">';
        s.items.forEach(function (i) { h += link(i, 'sidebar-sub-link'); });
        h += '</div>';
      } else {
        h += '<a class="sidebar-page-link active" href="' + ROOT + s.page + '">' + esc(s.label) + '</a><!--SUB-->';
      }
    });

    /* The page's own anchors go directly under the row that is the page, and nowhere if the page
       carries none. `ia/annotations/*` has none: its sub list is route and is already drawn. */
    h = h.replace('<!--SUB-->', subHTML).replace(/<!--SUB-->/g, '');

    host.innerHTML =
      '<div class="sidebar-brand"><div class="sidebar-project-name">Prediction Market</div></div>' +
      '<nav class="sidebar-nav" aria-label="Course roadmap">' + h + '</nav>';
  }

  /* IT RENDERS NOW, NOT ON DOMContentLoaded, and the difference is not the flash. Thirteen of
     these pages carry an inline scrollspy at the foot of the body that takes
     `[...document.querySelectorAll('.sidebar-sub-link')]` ONCE, at parse time, and toggles
     `.active` on that captured list from an IntersectionObserver. A panel written after that line
     runs hands the spy a list of elements no longer in the document, and the section highlight
     dies on all thirteen with nothing in the console to say so. The script tag stands directly
     under the `<aside>` it fills, so the host is already parsed and this is simply the earliest
     correct moment. The fallback is for a page that moves the tag. */
  if (document.getElementById('sidebar')) {
    render();
  } else {
    document.addEventListener('DOMContentLoaded', render);
  }
})();
