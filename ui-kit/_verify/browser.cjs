/* ui-kit/_verify/browser.cjs - the ONE reader of the browser.

   WHY THIS FILE EXISTS. Every check in this project that had to ask a browser a
   question was written for one step and thrown away: the contrast sweep of step
   1, the focus sweep of step 2, the pixel proof of step 3, the pattern render of
   step 4, the guide render of step 5. Six instrument bugs were therefore found
   six times and fixed in six places, and at least two of them were the SAME bug
   discovered twice, because the file that had learned the lesson no longer
   existed when the next check was written.

   This is the same move _levels.py made for containment: one computation, many
   consumers. Nothing here measures a product decision. It only knows how to ask
   correctly, and every rule below is a scar.

   THE TWELVE THINGS IT KNOWS, and the case that taught each one:

   1. A COLOUR IS PARSED BY A CANVAS, NEVER BY A REGEX.
      getComputedStyle returns what the AUTHOR wrote, and color-mix(in oklab, ...)
      comes back verbatim. Pulling numbers out of that string yields oklab
      components that contrast maths reads as sRGB bytes. Step 1 reported a focus
      ring at 2.72:1 that measures 6.95:1, and rejected three real rings while it
      was at it. The browser's own parser is the only correct one.

   2. ALPHA IS COMPOSITED UP THE ANCESTOR STACK.
      A translucent fill over a translucent tint over a plate is three colours,
      and the ratio is against what is actually behind the glyph. Reading only
      the element's own background reported a brass ring on a selected YES at
      1.37:1 (step 2), because the ground it measured was the control's own fill
      rather than the surface the ring is drawn on.

   3. INERT SUBTREES ARE SKIPPED, AND FOCUS IS A REAL TAB.
      A closed <dialog>, [hidden], [inert] and aria-hidden are not on screen and
      not in the tab order. Scripted .focus() reaches elements a person cannot,
      and it does not fire :focus-visible the way the keyboard does, which is the
      only selector the system declares (base.css:44).

   4. BOTH BATCHES OF A COMPARISON RUN IN THE SAME REGIME: fresh context, cache
      disabled, every time.
      Step 3 measured nine screens 7,500 to 11,200 pixels apart because -before
      was shot in a reused page with a warm cache and -after in a fresh one. Same
      regime: every one collapsed to 0, 4, 11, 42 or 83. The mirror is worse: a
      stale stylesheet invented a .tc-page defect (margin 16px -> 0px) and can
      equally HIDE one by making after look exactly like before.

   5. MEASURE AFTER THE THEME TRANSITION HAS SETTLED, NOT AT THE MOMENT OF THE
      SWITCH.
      Components transition colour. Reading straight after flipping data-theme
      reads the tween: step 2 flagged 17 focus rings that were fine, and step 5
      reported the jump chips at 2.58:1 in daylight where they measure 7.14:1
      once the transition ends. This one was learned twice, which is the whole
      argument for this file.

   6. A COLOUR PAINTED THROUGH A BLEND OR A FILTER CANNOT BE READ FROM `color`.
      mix-blend-mode and filter change the pixel AFTER the cascade, so
      getComputedStyle reports a colour the screen never shows. The very first
      full sweep of the vitrine reported 24 defects on the ramp labels of
      tokens.html, which are mix-blend-mode:difference and are legible. Those
      elements are returned marked `blended` and counted apart: a measurement
      that cannot be taken is reported as not taken, never as a pass and never
      as a failure.

   7. A CONSOLE ERROR IS ATTRIBUTED BY URL, NEVER BY ITS TEXT.
      "Failed to load resource: 404" does not say which file, and page.url() at
      message time is whatever page the loop has reached. Step 4 spent a pass
      chasing a 404 on patterns.html that was /favicon.ico, which the browser
      asks for on its own and a dev server does not have.

   8. A GRADIENT IS NOT A BACKGROUND-COLOUR. Written in full beside the code that
      does it, because that is where a person deleting it will be standing.

   9. A CONTRAST SWEEP CANNOT SEE A THING THAT IS PINNED OUT OF REACH.
      Every check this file had was about the pixel: the colour of it, the ring
      round it, the request behind it. All three pass on an element nobody can
      scroll to. ui-visual/terms.html shipped a contents rail 601px tall, pinned
      at top:120px with no cap and no inner scroll, and audit.cjs called the page
      clean twice: the rail needs 721px of window height, so on a 1366x768 laptop
      rows 12, 13 and 14 of a fourteen-row contents are off the bottom of the
      screen for the first 3,500px of a 4,884px document. Nothing was miscoloured
      and nothing overflowed sideways. The defect is GEOMETRY, and it is
      mechanical: a sticky or fixed box needs offset + height pixels of window,
      and if it has no auto/scroll of its own it can never give the rest back.
      Reported as `needs`, so one measurement answers it at any window size, and
      the floor it is compared against is a product decision that lives at the
      foot of this file with the contrast floor.

  10. TEXT THAT PAINTS NOTHING HAS NO CONTRAST.
      Found by running check 9 across the product, which is the argument for
      running a new check everywhere rather than on the page that prompted it.
      components/card.css:23 sets the event thumbnail to color:transparent and
      font-size:0, because the span carries the words "thumbnail placeholder" for
      a reader who cannot see the photograph and the photograph is a background
      image. The sweep read a text node, measured transparent ink on the photo
      and reported 1:1, on every card on every feed screen. Same answer as 6 and
      8: a measurement that cannot be taken is reported as not taken. Counted,
      never failed, so a span that goes transparent by accident is still visible
      in the number rather than swallowed by it.

  11. A HOVER IS A POINTER, AND NOTHING ELSE RAISES IT.
      The sibling of 3, and it arrived the same way: a pass that merged the
      button family had its whole intended change inside :hover, and snap.cjs
      measures the rest state, so the diff that proves nothing moved is also
      blind to the one thing that did. There is no class to add and no property
      to set: :hover is the browser's answer to a real mouse position, so the
      mouse is moved to the middle of the box and the value is read after the
      transition the rule declares. Reading it any earlier reads the tween,
      which is lesson 5 in a second place.

  12. THE CODE THAT IMPLEMENTS LESSON 5 WAS MEASURING NOTHING, for two reasons
      at once, and it had been since the day it was written. settleMs() returns
      the longest transition the document declares, and it returned 0.
      First: it read the declaration TEXT, and every transition in this system
      is written with a token, so the scan matched no number anywhere.
      Second, and worse: two of its three regexes reached the browser without
      their backslashes. Everything below is a TEMPLATE LITERAL, and a lone
      backslash-d in one is an escape sequence node swallows, so /^[\\d.]+m?s$/
      arrived as /^[d.]+m?s$/ and matched nothing that could exist.
      Third, found while fixing the first two: the walk recursed on
      rule.cssRules, which only @media and @supports used to have. Chrome ships
      CSS Nesting, so every style rule now carries an EMPTY list, an empty list
      is truthy, and 1263 of 1285 rules were skipped before their declarations
      were read.
      Consequence: every theme switch in this repo has waited 120ms where the
      document asks for 300, and every measurement taken after one was taken
      while the colour was still moving. Nothing published was wrong by it,
      because the values that were read had already arrived, but the guard was
      not there. A checker with a broken instrument reports clean.

   None of the twelve is defensive coding. Each is a wrong answer this project
   has already published, and anyone who removes one as excessive caution should
   read the line above it first.

   Usage from another script in this folder:

       const B = require('./browser.cjs');
       const s = await B.open({ width: 1440, theme: 'light' });
       const bad = await s.page.evaluate(B.PROBE + '; __ask.contrast()');
       await s.close();

   No em dash.
*/
const { chromium } = require(process.env.PLAYWRIGHT_MODULE
  || '/Users/sergiyshevchenko/.npm/_npx/9833c18b2d85bc59/node_modules/playwright');

/* ---------------------------------------------------------------- in-page --
   Everything that needs the DOM, as a source string. It is a string and not an
   imported function because it runs inside the page, and it is exported so the
   scripts that snapshot properties and the scripts that measure colour cannot
   drift into two different ideas of what "the ground behind this glyph" means. */
const PROBE = `
window.__ask = (function () {
  /* 1. the browser's own parser */
  var cv = document.createElement('canvas').getContext('2d', { willReadFrequently: true });
  function px(css) {
    cv.clearRect(0, 0, 1, 1);
    cv.fillStyle = '#000';
    try { cv.fillStyle = css; } catch (e) { return [0, 0, 0, 1]; }
    cv.fillRect(0, 0, 1, 1);
    var d = cv.getImageData(0, 0, 1, 1).data;
    return [d[0], d[1], d[2], d[3] / 255];
  }
  function lum(c) {
    function f(v) { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); }
    return 0.2126 * f(c[0]) + 0.7152 * f(c[1]) + 0.0722 * f(c[2]);
  }
  function over(fg, bg) {
    var a = fg[3];
    return [fg[0] * a + bg[0] * (1 - a), fg[1] * a + bg[1] * (1 - a), fg[2] * a + bg[2] * (1 - a), 1];
  }
  /* 2. composite up the stack until something is opaque */
  function ground(el, skipSelf) {
    var n = skipSelf ? el.parentElement : el, stack = [];
    while (n) {
      var c = px(getComputedStyle(n).backgroundColor);
      if (c[3] > 0) stack.push(c);
      if (c[3] >= 0.999) break;
      n = n.parentElement;
    }
    if (!stack.length || stack[stack.length - 1][3] < 0.999) stack.push(px('#000'));
    var out = stack.pop();
    while (stack.length) out = over(stack.pop(), out);
    return out;
  }
  function ratio(a, b) {
    var l1 = lum(a), l2 = lum(b), hi = Math.max(l1, l2), lo = Math.min(l1, l2);
    return (hi + 0.05) / (lo + 0.05);
  }
  /* 3. what a person can actually see and reach */
  function inert(el) {
    for (var n = el; n; n = n.parentElement) {
      if (n.hasAttribute && (n.hasAttribute('inert') || n.hasAttribute('hidden'))) return true;
      if (n.getAttribute && n.getAttribute('aria-hidden') === 'true') return true;
      if (n.tagName === 'DIALOG' && !n.open) return true;
      var s = getComputedStyle(n);
      if (s.display === 'none' || s.visibility === 'hidden') return true;
    }
    return false;
  }
  /* 6. the pixel is decided after the cascade, so the computed colour is not
        what the screen shows. Note the wording: no backtick, because this
        comment lives inside the template literal that carries the probe and a
        backtick here ends the string. */
  /* 8. AND A GRADIENT IS NOT A BACKGROUND-COLOUR. ground() composites
        backgroundColor up the stack, and an element painted with
        background-image:linear-gradient() computes backgroundColor to
        transparent, so the walk goes straight past it and measures the label
        against whatever is BEHIND the button. Found on 2026-08-03 accepting
        ui-visual/terms.html: .auth-btn.primary reported 1.18:1 and the flat
        .cta-bar button 1.05:1, on a brass gradient with dark ink that actually
        measures about 5.5:1. Both were false. Same family as 7 and the same
        answer: the painted pixel is not the computed value, so the element is
        UNMEASURABLE from the cascade rather than failing. A gradient ground
        needs a sampled pixel, and that is a different instrument. */
  function gradient(s) {
    var b = s.backgroundImage;
    return !!b && b !== 'none' && /gradient\\(/.test(b);
  }
  function blended(el) {
    for (var n = el; n; n = n.parentElement) {
      var s = getComputedStyle(n);
      if (s.mixBlendMode && s.mixBlendMode !== 'normal') return true;
      if (s.filter && s.filter !== 'none') return true;
      if (s.backdropFilter && s.backdropFilter !== 'none') return true;
      /* only where it would be READ as the ground: an opaque colour below the
         gradient ends the walk anyway, so a gradient on a page-level plate does
         not blind every label inside it. */
      if (gradient(s)) {
        var c = px(s.backgroundColor);
        if (c[3] < 0.999) return true;
      }
      if (px(getComputedStyle(n).backgroundColor)[3] >= 0.999) return false;
    }
    return false;
  }
  function paintsText(el) {
    for (var i = 0; i < el.childNodes.length; i++) {
      var n = el.childNodes[i];
      if (n.nodeType === 3 && n.textContent.trim()) return true;
    }
    return false;
  }
  function label(el) {
    return (el.tagName.toLowerCase() + (el.className && el.className.baseVal === undefined
      ? '.' + String(el.className).trim().split(/\\s+/).join('.') : '')).slice(0, 60);
  }

  var UA_LINK = { 'rgb(0, 0, 238)': 1, 'rgb(85, 26, 139)': 1, 'rgb(0, 0, 255)': 1 };

  return {
    px: px,
    /* every element that paints text of its own, with the ratio against the
       colour actually behind it. Skips what nobody can see. */
    contrast: function (root) {
      var out = [];
      var all = (root ? document.querySelector(root) : document).querySelectorAll('*');
      for (var i = 0; i < all.length; i++) {
        var el = all[i];
        if (!paintsText(el) || inert(el)) continue;
        var box = el.getBoundingClientRect();
        if (!box.height) continue;
        var cs = getComputedStyle(el);
        var bg = ground(el, false);
        var ink = px(cs.color);
        var fg = over(ink, bg);
        out.push({ el: label(el), text: el.textContent.trim().slice(0, 40),
                   ratio: +ratio(fg, bg).toFixed(2), blended: blended(el),
                   /* 10. transparent ink or a zero face draws no glyph */
                   unpainted: ink[3] === 0 || parseFloat(cs.fontSize) === 0,
                   size: parseFloat(cs.fontSize), weight: cs.fontWeight });
      }
      return out;
    },
    /* a link with no rule behind it is still painted, by the User Agent. It is
       nowhere in the repository, so no source scan can find it. */
    uaLinks: function () {
      var out = [], a = document.querySelectorAll('a');
      for (var i = 0; i < a.length; i++) {
        if (UA_LINK[getComputedStyle(a[i]).color] && paintsText(a[i]) && !inert(a[i])) {
          out.push({ el: label(a[i]), text: a[i].textContent.trim().slice(0, 40) });
        }
      }
      return out;
    },
    /* the ring is measured against the surface it STANDS ON, which with
       outline-offset >= 0 is the parent stack and not the control's own fill. */
    ring: function () {
      var el = document.activeElement;
      if (!el || el === document.body) return null;
      var cs = getComputedStyle(el);
      var offset = parseFloat(cs.outlineOffset) || 0;
      var bg = ground(el, offset >= 0);
      var ring = over(px(cs.outlineColor), bg);
      return { el: label(el), width: cs.outlineWidth, style: cs.outlineStyle,
               offset: cs.outlineOffset, ratio: +ratio(ring, bg).toFixed(2),
               visible: cs.outlineStyle !== 'none' && parseFloat(cs.outlineWidth) > 0 };
    },
    /* 11. the two halves of a hover measurement. paint() marks every visible
       match with an index and hands back the box centre for the pointer and the
       five values a control's rest state is made of; paintAt() reads the same
       five back once the mouse is on it. Marking rather than re-querying,
       because a selector that matched twelve elements before the pointer moved
       has to mean the same twelve after. */
    paint: function (sel) {
      var out = [], all = document.querySelectorAll(sel);
      for (var i = 0; i < all.length; i++) {
        var el = all[i], b = el.getBoundingClientRect();
        if (!b.width || !b.height || inert(el)) continue;
        el.setAttribute('data-paint', String(i));
        var cs = getComputedStyle(el);
        var scope = ['dialog', '.bet-dock', '.bet-panel', '.bet-sheet', '.cta-bar',
                     '.app-header', '.state-block'];
        var where = 'plain';
        for (var s = 0; s < scope.length; s++) {
          var up = el.closest(scope[s]);
          if (up) { where = scope[s] + (up.className ? '.' + String(up.className).split(' ')[1] || '' : ''); break; }
        }
        out.push({ i: i, el: label(el), scope: where,
                   x: Math.round(b.left + b.width / 2), y: Math.round(b.top + b.height / 2),
                   rest: [cs.backgroundColor, cs.backgroundImage.slice(0, 50), cs.borderTopColor,
                          cs.borderTopWidth, cs.color].join(' | ') });
      }
      return out;
    },
    paintAt: function (i) {
      var el = document.querySelector('[data-paint="' + i + '"]');
      if (!el) return null;
      var cs = getComputedStyle(el);
      return [cs.backgroundColor, cs.backgroundImage.slice(0, 50), cs.borderTopColor,
              cs.borderTopWidth, cs.color].join(' | ');
    },
    deadIcons: function () {
      var out = [], u = document.querySelectorAll('use');
      for (var i = 0; i < u.length; i++) {
        var h = u[i].getAttribute('href') || u[i].getAttribute('xlink:href') || '';
        if (h.charAt(0) === '#' && !document.getElementById(h.slice(1))) out.push(h);
      }
      return out;
    },
    overflowX: function () {
      var d = document.documentElement;
      return d.scrollWidth - d.clientWidth;
    },
    /* 9. every pinned box, with the window height it needs and the window it was
          measured in. ASK IT IN THE SHORT WINDOW: the first version of this
          computed needs = offset + height in a 900px pass and compared the
          number against a 640px floor, which reported both modal dialogs as
          stranded. They are not. Both are capped in viewport-relative units
          (max-height:calc(100% - 38px)) and hand their overflow to .sheet-body,
          so they shrink with the window and always fit; the 752px they measured
          was 752px of a window that was 900px tall. Reading the cap back out of
          getComputedStyle does not separate the two cases either, because a
          plain 92vh resolves to px and only a calc() survives as itself. The
          window is the instrument: render at the floor and the capped box fits
          while the pinned rail hangs out the bottom, no unit sniffing anywhere.
          scrollHeight and not just the border box, because a box capped with
          overflow:hidden measures short and hides its tail anyway.
          A box with no top and no bottom is not pinned vertically and is not
          this check's business. */
    pinned: function () {
      var out = [], all = document.querySelectorAll('*');
      for (var i = 0; i < all.length; i++) {
        var el = all[i], s = getComputedStyle(el);
        if (s.position !== 'sticky' && s.position !== 'fixed') continue;
        if (inert(el)) continue;
        var b = el.getBoundingClientRect();
        if (!b.height) continue;
        var anchor = null, off = 0;
        if (s.top !== 'auto' && !isNaN(parseFloat(s.top))) { anchor = 'top'; off = parseFloat(s.top); }
        else if (s.bottom !== 'auto' && !isNaN(parseFloat(s.bottom))) { anchor = 'bottom'; off = parseFloat(s.bottom); }
        if (anchor === null) continue;
        var h = Math.max(b.height, el.scrollHeight);
        out.push({ el: label(el), position: s.position, anchor: anchor,
                   offset: +off.toFixed(1), height: +h.toFixed(1),
                   needs: Math.ceil(off + h), vh: window.innerHeight,
                   scrolls: /auto|scroll/.test(s.overflowY) || /auto|scroll/.test(s.overflow) });
      }
      return out;
    },
    /* The longest transition the document DECLARES, so the caller waits a
       measured time instead of a guessed one.

       Read from the stylesheets and not by walking the DOM, for two reasons.
       There are a few hundred rules and several thousand elements, and a full
       walk made a sweep of the vitrine take minutes. And a rule that is not
       applied to anything right now still applies the moment a state changes,
       so the CSSOM is the more correct question as well as the cheaper one.

       DESCEND INTO CSSImportRule.styleSheet. Everything in this system arrives
       through the @imports of components/index.css, so a scan that reads only
       document.styleSheets sees the entry point and nothing in it. This project
       has already published one wrong answer that way: a CSSOM sweep reported
       "no margin rule matches" for a rule that was loaded. */
    settleMs: function () {
      var ms = 0;
      function num(v) {
        v = String(v).trim();
        return parseFloat(v) * (v.indexOf('ms') > -1 ? 1 : 1000) || 0;
      }
      function walk(sheet) {
        var rules;
        try { rules = sheet.cssRules; } catch (e) { return; }   // a cross-origin sheet
        if (!rules) return;
        for (var i = 0; i < rules.length; i++) {
          var r = rules[i];
          if (r.styleSheet) { walk(r.styleSheet); continue; }   // @import
          /* A STYLE RULE HAS cssRules TOO, and that is why this function
             returned 0 for the whole of this project. The line here used to
             recurse on cssRules alone and then continue, written when only
             @media and @supports had children. Chrome ships CSS Nesting now, so every
             CSSStyleRule carries an EMPTY CSSRuleList, an empty list is truthy,
             and every ordinary rule took the grouping branch and was skipped
             before its declarations were ever read. 46 stylesheets walked, 1285
             rules with declarations, 22 of them reached.
             Measured, not deduced: the hover pass read a border at
             rgba(199,162,78,0.467) where the only value in the system is 0.45,
             which is a tween, which is what a measurement is not allowed to
             read. So the length is asked as well as the existence, and the
             recursion no longer eats the rule it was meant to pass through. */
          if (r.cssRules && r.cssRules.length) walk(r);         // @media, @supports, nesting
          if (!r.style) continue;
          ['transition-duration', 'transition-delay', 'animation-duration',
           'transition', 'animation'].forEach(function (p) {
            var v = r.style.getPropertyValue(p);
            if (!v) return;
            /* THE BACKSLASHES ARE DOUBLED AND THEY HAVE TO BE. This whole probe
               is a TEMPLATE LITERAL, so a single backslash-s written once is
               parsed by node as an escape sequence, which it is not, and the
               page receives the bare letter: this pattern arrived in the browser
               as /^[d.]+m?s$/ and matched no duration ever written. Two of the
               three regexes in this function were wrong that way from the day it
               was written, which is the other half of why it returned 0. A regex
               inside this string is code twice, and the first reader is node. */
            v.split(',').forEach(function (one) {
              one.split(/\\s+/).forEach(function (tok) {
                if (/^[\\d.]+m?s$/.test(tok)) { var n = num(tok); if (n > ms) ms = n; }
              });
            });
          });
          /* A DURATION WRITTEN AS A TOKEN IS INVISIBLE TO A SCAN OF THE RULE.
             The loop above reads the declaration TEXT, and every transition in
             this system is written "transition:background var(--dur-quick)
             ease", so the token is the token and never a number: the scan
             matched nothing and this function returned the largest literal
             anyone happened to leave behind. Found on 2026-08-03 by the hover
             pass, which read border-colour at rgba(...,0.467) where the only
             value in the system is 0.45 - the tween, which is exactly what
             lesson 5 says a measurement must not read, taken by the code that
             implements lesson 5. So the custom properties are read too, from
             the same rules, and the longest duration the sheet declares under
             ANY name is what a measurement waits for. */
          for (var d = 0; d < r.style.length; d++) {
            var prop = r.style[d];
            if (prop.slice(0, 2) !== '--') continue;
            var raw = r.style.getPropertyValue(prop).trim();
            if (/^[\\d.]+m?s$/.test(raw)) { var t = num(raw); if (t > ms) ms = t; }
          }
        }
      }
      for (var s = 0; s < document.styleSheets.length; s++) walk(document.styleSheets[s]);
      return Math.ceil(ms);
    }
  };
})();
`;

/* ------------------------------------------------------------- node side -- */
let _browser = null;

async function browser() {
  if (!_browser) _browser = await chromium.launch({ channel: 'chrome' });
  return _browser;
}

/* A SESSION IS ALWAYS A FRESH CONTEXT WITH THE CACHE OFF. Not an option, and
   there is no flag to turn it back on: the only reason to reuse a context is
   speed, and lesson 4 above is what speed cost. */
async function open(opts) {
  opts = opts || {};
  const b = await browser();
  const context = await b.newContext({
    viewport: { width: opts.width || 1440, height: opts.height || 900 },
    deviceScaleFactor: opts.scale || 1
  });
  const page = await context.newPage();
  const cdp = await context.newCDPSession(page);
  await cdp.send('Network.enable');
  await cdp.send('Network.setCacheDisabled', { cacheDisabled: true });

  /* 6. attributed by URL. A console message says a request failed and not which
     one, so the responses are recorded instead, and the browser's own automatic
     favicon probe is not a defect of any page. */
  const failed = [], errors = [];
  page.on('response', (r) => {
    if (r.status() >= 400 && !/\/favicon\.ico(\?|$)/.test(r.url())) {
      failed.push({ status: r.status(), url: r.url(), from: r.request().frame() ? r.request().frame().url() : null });
    }
  });
  page.on('console', (m) => {
    if (m.type() !== 'error') return;
    if (/Failed to load resource/.test(m.text())) return;   // the response listener owns those
    errors.push({ url: page.url(), text: m.text().slice(0, 200) });
  });
  page.on('pageerror', (e) => errors.push({ url: page.url(), text: String(e).slice(0, 200) }));

  await page.addInitScript(PROBE);

  const session = {
    page, context, failed, errors,
    async go(url, theme) {
      await page.goto(url, { waitUntil: 'networkidle' });
      if (theme) await session.theme(theme);
      return session;
    },
    /* 5. set it, then wait for what the document itself says is the longest
       transition. Reading at the moment of the switch reads the tween. */
    async theme(name) {
      await page.evaluate((t) => document.documentElement.setAttribute('data-theme', t), name);
      const ms = await page.evaluate('__ask.settleMs()');
      await page.waitForTimeout(Math.max(ms, 60) + 120);
      return session;
    },
    /* 3. a real Tab. Scripted .focus() reaches what a person cannot and does not
       raise :focus-visible, which is the only focus selector this system has. */
    async tab(n) {
      for (let i = 0; i < (n || 1); i++) await page.keyboard.press('Tab');
      return page.evaluate('__ask.ring()');
    },
    /* 11. and a real pointer, for the same reason. Takes the index paint() put
       on the element rather than a coordinate, because A POINTER ONLY REACHES
       WHAT IS IN THE WINDOW: the first cut moved the mouse to the box centre
       paint() reported, which is viewport-relative, so every control below the
       fold was pointed at from outside the window and reported its rest state
       as its hover. Two buttons on how-it-works.html read that way and it looks
       exactly like a missing rule. The element is scrolled into view first.
       The wait is the document's own declared transition and not a guess. */
    async hoverAt(i) {
      const el = await page.$('[data-paint="' + i + '"]');
      if (!el) return null;
      try { await el.hover({ timeout: 2000 }); } catch (e) { return null; }
      const ms = await page.evaluate('__ask.settleMs()');
      await page.waitForTimeout(Math.max(ms, 60) + 60);
      return page.evaluate('__ask.paintAt(' + i + ')');
    },
    /* the mouse off everything, so the next measurement starts from rest */
    async unpoint() { await page.mouse.move(1, 1); return session; },
    ask(expr) { return page.evaluate('__ask.' + expr); },
    async close() { await context.close(); }
  };
  return session;
}

async function shutdown() {
  if (_browser) { await _browser.close(); _browser = null; }
}

/* AA for body text, and 3:1 for large text and for a graphic. Written here so
   three scripts cannot each pick their own floor. */
function floorFor(size, weight) {
  const bold = parseInt(weight, 10) >= 700;
  return (size >= 24 || (size >= 18.66 && bold)) ? 3 : 4.5;
}

/* The shortest window a pinned box has to fit inside, for lesson 9. Same reason
   as floorFor: one number, not one per script.
   640 is the 1366x768 laptop, still the commonest small desktop screen, with
   about 120px of browser chrome taken off it. Chosen as a floor and not as a
   target: everything in this product that is pinned to the top of a window
   should fit a screen that ordinary, and anything that does not has to say so
   out loud. */
const SHORTEST_VIEWPORT = 640;

module.exports = { PROBE, open, browser, shutdown, floorFor, SHORTEST_VIEWPORT };
