/* ui-kit/_nav.js - the ONE registry of the stand, and the only copy of it.

   WHAT THIS IS NOT. A file of this name lived here until 2026-08-07 and was
   deleted with the instrument. It was deleted for the right reason and it was
   not this file: it was the OUTPUT of `_gen_component_pages.py`, which wrote 38
   pages and then wrote the registry, and the archive states the rule it lived
   under out loud, "`_nav.js` is rebuilt, not edited". A generated file cannot be
   corrected by hand, because the next run puts it back; that is how a
   hand-applied voice rewrite was silently reverted in this repository.

   THIS FILE WRITES NOTHING AND NOTHING WRITES IT. It is read by a browser at
   load and it is edited by a person. That is the whole difference between a
   machine and a piece of furniture, and the rule the kit keeps ("a page is
   written by hand, no generator, ever") is about the first one.

   WHY IT EXISTS AT ALL, in one measurement. `ui-visual` carries the same screen
   list hand-copied into 106 pages, 1,339 KB of it, and `wireframes` carries its
   own into 104, 1,247 KB. Neither has drifted, and neither could have stayed in
   step by hand: `_resync_sidebar.py` held them, and it was deleted too. The kit
   had seven pages when this was written, twelve on 2026-08-08 and nineteen by
   the end of the same day, on the way to 55.
   Nineteen copies of one list would be nineteen edits for every row, and the root rule says
   a fact written twice will drift. So the list is written once, here, and no page
   of the stand declares any part of it. THE SENTENCE ABOVE HAS BEEN CORRECTED
   THREE TIMES ALREADY, which is the argument standing up on its own.

   THE STAND PAGE DECLARES NOTHING, not even its own name. It carries an empty
   `<aside class="sidebar" id="rmSidebar">` and loads this file.

   TWO THINGS TAKEN FROM THE SAME PANEL IN THE Stack REPOSITORY, because both
   were paid for there and neither has to be paid for twice:

   1. THE ACTIVE ROW IS COMPUTED FROM THE FILE NAME, never declared. Every page
      there hand-wrote a `KIT_ACTIVE` constant; one page was built from another
      and inherited its value, so the panel lit one row while showing a different
      component. A file name cannot be a stale copy, because it IS the page.
   2. A ROW WITH NO PAGE IS VISIBLE, as a `<span>` with the `.planned` badge that
      `course-chrome.css` already draws. Hiding it would make the panel look
      finished and lie about it.

   AND ONE THING NOT TAKEN. That panel writes `style="opacity:.45"` on the rows
   it dims. Never on the element, and it is not needed: `.sidebar-page-link
   .planned` is the muted ROLE with a badge, and the reason is written above the
   rule in `course-chrome.css` - opacity fades text into its ground and takes
   --chrome-muted from 5.03:1 to 2.69:1, which no sweep reading `.color` can see.

   NO CSS OF ITS OWN. Every class below is `course-chrome.css`, which
   `components/index.css` already imports and every kit page already loads and
   until now used nothing of. The 220px inset is `base.css`, which insets any
   body that contains `#rmSidebar`.

   No em dash in this file. */

window.KIT_NAV = [
  {
    label: 'Foundations',
    items: [
      { label: 'Colour',     page: 'colour.html',     done: true, note: '133 roles' },
      { label: 'Typography', page: 'typography.html', done: true, note: '3 families' },
      { label: 'Geometry',   page: 'geometry.html',   done: true, note: '4px grid' },
      { label: 'Icons',      page: 'icons.html',      done: true, note: '52 glyphs' }
    ]
  },
  {
    /* A LEVEL IS A SHELF AND A COMPONENT IS A PAGE, and the two answer different
       questions. This panel said the opposite until 2026-08-08: "a page per
       LEVEL, not per component, because forty pages of one component each are
       forty navigations to compare two chips". THE REASON WAS RIGHT AND IT WAS
       A REASON FOR THE SHELF, not against the pages. Comparing ten atoms is
       what a level page is for, and it keeps that job; taking ONE apart needs
       room a shelf does not have, because a shelf gives every component one
       specimen and one rule.

       THE COUNTED THRESHOLD IS DEAD, and one component killed it. It used to
       say: a page of its own is earned by being one of the largest families,
       902, 1,361 and 1,679 placements, and "a component with one face does not
       get a page here, however often it is worn". Then `toast` was written:
       FOUR placements on ONE screen, and its page carries where the boundary
       with its own dismiss runs, why its error face is not red, and the fact
       that most of the component is a behaviour no static page can draw. None
       of that is a function of how often it is worn. `toggle` settles it: 3
       placements, and FOUR of its five faces have no placement in the product
       at all, so a stand built by walking screens would show one grey oval and
       call it the component.

       SO EVERY COMPONENT GETS A ROW HERE, and a row with no page renders as a
       <span> with a badge, which is the whole reason this panel lists things
       that do not exist yet. The level page is the first row of its own group,
       named "All ...", because it is a page like the others and the group would
       otherwise have a title nobody could click. */
    label: 'Atoms',
    items: [
      { label: 'All atoms',   page: 'vitrine.html', done: true, note: '10' },
      { label: 'Button',      page: 'button.html',  done: true, note: '902' },
      { label: 'Icon button', page: 'iconbtn.html', done: true, note: '1,361' },
      { label: 'Chip',        page: 'chip.html',    done: true, note: '1,679' },
      { label: 'Nav item',    page: 'navitem.html', done: true, note: '995' },
      { label: 'Odds bar',    page: 'oddsbar.html', done: true, note: '72' },
      { label: 'Input',       page: 'input.html',   done: true, note: '122' },
      { label: 'Yes / No',    page: 'yesno.html',   done: true, note: '116' },
      { label: 'Toast',       page: 'toast.html',   done: true, note: '4' },
      { label: 'Skeleton',    page: 'skeleton.html',done: true, note: '482' },
      { label: 'Toggle',      page: 'toggle.html',  done: true, note: '3' }
    ]
  },
  {
    /* A PLANNED ROW STILL CARRIES ITS PAGE NAME, which is the name the file will
       have and not a guess: `row()` never reads it while `done` is false, and
       writing it now is how the next person building one knows what to call it.

       THE LAST THREE OF THIS GROUP HAD NO SHELF SECTION EITHER, AND NOW THEY DO.
       `account`, `cookie-consent` and `toc` were three of the six that
       `ui-kit/docs/inventory.md` called "outside the core, unmeasured": they
       stand on none of the five anchor screens, so "holds nothing" was not a
       reading anybody had taken about them, and a level printed without a
       reading is a guess wearing a declaration's clothes. They were WALKED on
       2026-08-08, on the six screens that do carry them, containment read from
       the DOM: all three hold something and all three are level 2. The shelf
       gained three sections the same day and the word came off. */
    label: 'Molecules',
    items: [
      { label: 'All molecules', page: 'molecules.html', done: true, note: '17' },
      { label: 'Trust bar',     page: 'trustbar.html',   done: true, note: '525' },
      { label: 'Market',        page: 'market.html',     done: true, note: '9' },
      { label: 'Comments',      page: 'comments.html',   done: true, note: '36' },
      { label: 'Notice',        page: 'notice.html',     done: true, note: '250' },
      { label: 'Filters',       page: 'filters.html',    done: true, note: '193' },
      { label: 'Bottom nav',    page: 'bottomnav.html',  done: true, note: '105' },
      { label: 'Category nav',  page: 'catnav.html',     done: true, note: '57' },
      { label: 'Related',       page: 'related.html',    done: true, note: '31' },
      { label: 'State block',   page: 'state-block.html',done: true, note: '38' },
      { label: 'Position',      page: 'position.html',   done: true, note: '57' },
      { label: 'Quick amounts', page: 'quick.html',      done: true, note: '480' },
      { label: 'Options',       page: 'options.html',    done: true, note: '52' },
      { label: 'SEO plate',     page: 'seo-plate.html',  done: true, note: '36' },
      { label: 'Load more',     page: 'loadmore.html',   done: true, note: '9' },
      { label: 'Account',       page: 'account.html',    done: true, note: '3' },
      { label: 'Cookie consent',page: 'cookie-consent.html', done: true, note: '1' },
      { label: 'Contents',      page: 'toc.html',        done: true, note: '14' }
    ]
  },
  {
    label: 'Organisms',
    items: [
      { label: 'All organisms', page: 'organisms.html',    done: true, note: '13' },
      { label: 'Header',        page: 'header.html',       done: false, next: true },
      { label: 'Footer',        page: 'footer.html',       done: false },
      { label: 'Dialog',        page: 'dialog.html',       done: false },
      { label: 'How it works',  page: 'hiw-dialog.html',   done: false },
      { label: 'Tabs',          page: 'tabs.html',         done: false },
      { label: 'Event detail',  page: 'event-detail.html', done: false },
      { label: 'Bet panel',     page: 'betpanel.html',     done: false },
      { label: 'Bets table',    page: 'bets-table.html',   done: false },
      { label: 'Chart',         page: 'chart.html',        done: false },
      { label: 'Card',          page: 'card.html',         done: false },
      { label: 'Hero',          page: 'hero.html',         done: false },
      { label: 'Feed',          page: 'feed.html',         done: false },
      { label: 'Profile',       page: 'profile.html',      done: false }
    ]
  },
  {
    label: 'Patterns',
    items: [
      { label: 'All patterns',  page: 'patterns.html',     done: true, note: '6' },
      { label: 'Action bar',    page: 'action-bar.html',   done: false },
      { label: 'Browse shell',  page: 'browse-shell.html', done: false },
      { label: 'Card grid',     page: 'card-grid.html',    done: false },
      { label: 'Detail shell',  page: 'detail-shell.html', done: false },
      { label: 'List head',     page: 'list-head.html',    done: false },
      { label: 'Position list', page: 'position-list.html',done: false }
    ]
  },
  {
    /* The reports are documents rather than stands, so they are indented. Each
       one is the artefact of a step, and a step whose artefact nobody can reach
       from the stand is a step that will be taken again. */
    label: 'The reports',
    kind: 'doc',
    items: [
      { label: 'Census',        page: 'docs/census.md',        done: true },
      { label: 'Inventory',     page: 'docs/inventory.md',     done: true },
      { label: 'Consolidation', page: 'docs/consolidation.md', done: true },
      { label: 'Audit',         page: 'docs/audit.md',         done: true }
    ]
  }
];

(function () {
  var K = 'pm-theme', root = document.documentElement;

  /* THEME FIRST AND BEFORE ANYTHING ELSE. This file is loaded from <head>, so
     this line runs before the first paint and daylight never flashes graphite.
     The kit's specimens pin their own `data-theme` on the figure, and
     `tokens.css` declares dark on `[data-theme="dark"]` as well as on :root
     precisely so a pinned subtree survives a themed ancestor. So the switch
     changes the stand around the pairs and never the pairs. */
  try { if (localStorage.getItem(K) === 'light') root.setAttribute('data-theme', 'light'); } catch (e) {}

  function lit() { return root.getAttribute('data-theme') === 'light'; }

  function render() {
    var nav = document.getElementById('rmSidebar');
    if (!nav) return;

    var file = (location.pathname.split('/').pop() || 'overview.html');
    /* The tally counts STAND PAGES, so the document groups are out of it and
       overview.html, which is not a row of any group, is in it. Counting the four
       reports as pages would make it 23 of 59 instead of 19 of 55 and mean less
       than either: a report is done or it does not exist, so it can only ever add
       the same number to both sides. */
    var total = 1, done = 1;
    window.KIT_NAV.forEach(function (g) {
      if (g.kind === 'doc') return;
      g.items.forEach(function (i) { total++; if (i.done) done++; });
    });

    var h =
      '<a class="sidebar-back" href="../research/research.html">' +
        '<span class="bk-arrow" aria-hidden="true">&larr;</span> Course roadmap</a>' +
      '<div class="sidebar-brand"><div class="sidebar-project-name">Design system - the kit</div></div>' +
      '<button type="button" class="theme-switch" aria-pressed="false">' +
        '<span class="ts-swatches" aria-hidden="true">' +
          '<span class="ts-sw ts-dark"></span><span class="ts-sw ts-light"></span></span>' +
        '<span class="ts-label">Vault</span></button>' +
      '<nav class="sidebar-nav" aria-label="The design system">' +
      row({ label: 'Overview', page: 'overview.html', done: true }, file, 'page');

    window.KIT_NAV.forEach(function (g) {
      var here = g.items.some(function (i) { return i.page === file; });
      var d = g.items.filter(function (i) { return i.done; }).length;
      var doc = g.kind === 'doc';
      h += '<div class="sidebar-divider' + (here ? ' active' : '') + '">' + g.label +
           (doc ? '' : ' ' + d + '/' + g.items.length) + '</div>';
      if (doc) h += '<div class="sidebar-sub">';
      g.items.forEach(function (i) { h += row(i, file, doc ? 'sub' : 'page'); });
      if (doc) h += '</div>';
    });

    /* The second sentence only exists while there IS a row with no page. A note
       explaining an absence that is not on screen is the panel talking about
       itself, and the first thing to go stale when the last row lands. */
    h += '</nav><p class="sidebar-note">' + done + ' of ' + total + ' stand pages written.' +
         (done < total ? ' A row with no page is a row that says so.' : '') + '</p>';

    nav.innerHTML = h;
    wireTheme();
    var cur = nav.querySelector('.active[href]');
    if (cur && cur.scrollIntoView) cur.scrollIntoView({ block: 'center' });
  }

  /* A NOT-DONE ROW IS A <span>, not a hidden row and not a dead link. `.planned`
     draws the Soon badge, `.planned.next` draws Next in brass, and both rules
     are already in course-chrome.css with their reasons. */
  function row(i, file, kind) {
    var cls = kind === 'sub' ? 'sidebar-sub-link' : 'sidebar-page-link';
    if (!i.done) {
      return '<span class="' + cls + ' planned' + (i.next ? ' next' : '') + '">' + i.label + '</span>';
    }
    var on = (i.page === file) ? ' active' : '';
    return '<a class="' + cls + on + '" href="' + i.page + '">' + i.label +
           (i.note ? '<i>' + i.note + '</i>' : '') + '</a>';
  }

  function wireTheme() {
    var b = document.querySelector('.theme-switch');
    if (!b) return;
    function paint() {
      b.setAttribute('aria-pressed', lit() ? 'true' : 'false');
      b.querySelector('.ts-label').textContent = lit() ? 'Daylight' : 'Vault';
    }
    b.addEventListener('click', function () {
      var on = lit();
      if (on) { root.setAttribute('data-theme', 'dark'); } else { root.setAttribute('data-theme', 'light'); }
      try { localStorage.setItem(K, on ? 'dark' : 'light'); } catch (e) {}
      paint();
    });
    paint();
  }

  /* THE HUB ROW, from the same registry as the panel. It only exists on
     overview.html, so the function is a no-op everywhere else. A row with no
     page renders as a <span>: `_page.css` draws it dashed, and the reason is
     the panel's reason, that a list of only the finished things looks finished. */
  function jump() {
    var el = document.getElementById('kitJump');
    if (!el) return;
    var file = (location.pathname.split('/').pop() || 'overview.html');
    var h = '';
    window.KIT_NAV.forEach(function (g) {
      g.items.forEach(function (i) {
        if (i.page === file) return;
        h += i.done ? '<a href="' + i.page + '">' + i.label + '</a>'
                    : '<span>' + i.label + '</span>';
      });
    });
    el.innerHTML = h;
  }

  /* The drawer below 860px. Above it `course-chrome.css` hides the toggle and
     the scrim with !important and pins the rail open, so this listener is inert
     rather than conditional. */
  function wireDrawer() {
    var sb = document.getElementById('rmSidebar'),
        ov = document.getElementById('rmOverlay'),
        tg = document.getElementById('rmToggle');
    if (!sb || !ov || !tg) return;
    tg.addEventListener('click', function () { sb.classList.add('open'); ov.classList.add('open'); });
    ov.addEventListener('click', function () { sb.classList.remove('open'); ov.classList.remove('open'); });
  }

  document.addEventListener('DOMContentLoaded', function () { render(); jump(); wireDrawer(); });
})();
