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

   THE SEVEN THINGS IT KNOWS, and the case that taught each one:

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

   None of the seven is defensive coding. Each is a wrong answer this project has
   already published, and anyone who removes one as excessive caution should read
   the line above it first.

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
        var bg = ground(el, false);
        var fg = over(px(getComputedStyle(el).color), bg);
        out.push({ el: label(el), text: el.textContent.trim().slice(0, 40),
                   ratio: +ratio(fg, bg).toFixed(2), blended: blended(el),
                   size: parseFloat(getComputedStyle(el).fontSize),
                   weight: getComputedStyle(el).fontWeight });
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
          if (r.cssRules) { walk(r); continue; }                // @media, @supports
          if (!r.style) continue;
          ['transition-duration', 'transition-delay', 'animation-duration',
           'transition', 'animation'].forEach(function (p) {
            var v = r.style.getPropertyValue(p);
            if (!v) return;
            v.split(',').forEach(function (one) {
              one.split(/\s+/).forEach(function (tok) {
                if (/^[\d.]+m?s$/.test(tok)) { var n = num(tok); if (n > ms) ms = n; }
              });
            });
          });
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

module.exports = { PROBE, open, browser, shutdown, floorFor };
