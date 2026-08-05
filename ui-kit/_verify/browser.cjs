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

   THE FOURTEEN THINGS IT KNOWS, and the case that taught each one:

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

  13. A BROKEN INSTRUMENT THAT REPORTS A DEFECT GETS CAUGHT. ONE THAT REPORTS ALL
      CLEAR IS CAUGHT BY NOBODY. Lessons 1, 6 and 12 were each found because
      somebody went to look at a finding and found the instrument lying instead.
      Nothing sends anybody to look at a zero. Fifteen printings of "0 below AA"
      stood across three documents while 378 elements measured under the floor,
      and the three bugs behind that zero were bugs THIS FILE had already
      recorded. The most dangerous output of a broken check is not a false
      alarm, it is a clean bill of health, and that is where verification effort
      belongs: not on what the checks report, but on what they are looking at.

  14. A PHOTOGRAPH OF A CROPPED SUBJECT LOOKS EXACTLY LIKE A PHOTOGRAPH, which
      is 13 arriving in pixels. boxAt() pads each side to at most HALF the
      distance to the nearest neighbour, which is right, and then let that
      halving win against the subject's own paint, which is not: the specimen
      row set a 14px gap, so every facing side was capped at 7px whatever the
      caller asked for, and the specimen page had no padding at all, so a
      control at x=0 got nothing. 36 of 790 state pictures were short, and every
      one of them was a FOCUS picture - the single state whose entire subject is
      a ring drawn OUTSIDE the box. The crop was in the png, so no change to the
      page displaying it could put back a pixel that was never captured, and
      nothing on that page could report it either.
      The pad is therefore DERIVED from the element being photographed, in the
      state it is in: extentAt() reads the computed outline and every non-inset
      shadow and returns the four sides. That is a FLOOR the neighbour rule may
      not go under, and what the frame actually managed is written into the
      manifest beside what it needed, so gate 31 can fail on a crop without a
      browser.

   None of the fourteen is defensive coding. Each is a wrong answer this project
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

  /* WHAT A CONTROL'S FACE IS MADE OF, in ONE place. It was written in three:
     five values here in paint(), the same five again in paintAt(), and six in
     states.cjs FACE(). Three copies of one idea, and they had already drifted by
     one property.

     AND THE FIVE WERE NOT ENOUGH, which is the defect this list grew for.
     components/button.css says the sign-in provider row lifts one pixel on hover
     and that the brass ones carry a glow, and ui-kit/authored/button.md names
     both as the thing that makes those members different. Neither transform nor
     boxShadow was in the five, so the instrument read four controls as ONE face
     while the document said they were four, and a merge on that reading would
     have deleted the pictures of a difference nobody could then see. Same shape
     as the false zero: a check reporting "identical" about a property it never
     looked at.

     opacity is here for the disabled fade, which is the only state this family
     expresses that way. Geometry that is only SIZE stays out on purpose: a
     different padding is the same face at a different size, and splitting on it
     would put one picture on the page twice. */
  function face(cs) {
    return [cs.backgroundColor, cs.backgroundImage.slice(0, 50), cs.borderTopColor,
            cs.borderTopWidth, cs.color, cs.borderTopLeftRadius,
            cs.transform, cs.boxShadow.slice(0, 60), cs.opacity].join(' | ');
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
        /* WHICH SCOPE THIS ONE STANDS IN, and named the way the stylesheet names
           it, because the scope is what decides the skin. The first cut built
           the name from the SECOND word of el.className, which is undefined
           on an element with a single class and the literal string
           "[object SVGAnimatedString]" on an svg, so half the scopes came out as
           "dialog.undefined". Empty when nothing matches, so a caller can fall
           back to something that means more than the word "plain".

           A STAND CLASS NEVER NAMES A PRODUCT GROUP. Every kit- class is this
           vitrine's own furniture: kit-nude is how a picked host gives up its
           surface, and it goes on the scope element itself. Without this filter
           the action bar's group came back as ".cta-bar.kit-nude" and the
           caption in the authored source had to spell a class the product does
           not have, on a group whose whole subject is a product control. It is
           filtered here rather than in states.cjs because the name is made here,
           and because the same treatment is about to reach 36 more pages. */
        var scope = ['dialog', '.bet-dock', '.bet-panel', '.bet-sheet', '.cta-bar',
                     '.app-header', '.state-block'];
        var where = '';
        for (var s = 0; s < scope.length; s++) {
          var up = el.closest(scope[s]);
          if (!up) continue;
          var base = scope[s].replace('.', '');
          var extra = (up.getAttribute('class') || '').split(/\\s+/)
            .filter(function (c) { return c && c !== base && c.indexOf('kit-') !== 0; });
          where = scope[s] + (extra.length ? '.' + extra[extra.length - 1] : '');
          break;
        }
        out.push({ i: i, el: label(el), scope: where,
                   x: Math.round(b.left + b.width / 2), y: Math.round(b.top + b.height / 2),
                   rest: face(cs) });
      }
      return out;
    },
    paintAt: function (i) {
      var el = document.querySelector('[data-paint="' + i + '"]');
      if (!el) return null;
      return face(getComputedStyle(el));
    },
    /* HOW FAR THIS ELEMENT PAINTS OUTSIDE ITS OWN BOX, per side, in the state it
       is in right now. Derived and never assigned, and derived from the SUBJECT
       rather than from a survey of the stylesheet, because the two answers are
       nothing like each other: a quiet button's brass hover glow reaches 7px
       below it and a dialog's plate shadow reaches 50, and a single number large
       enough for both would frame every control in a field of ground.
       Two sources, and they are the two things in this system that leave the box:
         the focus ring   outline-width + outline-offset, every side
         a drop shadow    offset + spread + blur/2 on the side it falls,
                          blur/2 being where a Gaussian of that radius has
                          faded out, which is what the spec makes the painting
                          area. An inset shadow paints INSIDE and is skipped.
       Returns four sides so a shadow that falls only downwards does not pad the
       top by the same amount and re-centre the subject in its own picture. */
    extentAt: function (i) {
      var el = document.querySelector('[data-paint="' + i + '"]');
      if (!el) return null;
      var cs = getComputedStyle(el);
      var need = { top: 0, right: 0, bottom: 0, left: 0 };
      var ow = parseFloat(cs.outlineWidth) || 0;
      if (ow && cs.outlineStyle !== 'none') {
        var ring = ow + (parseFloat(cs.outlineOffset) || 0);
        if (ring > 0) {
          need.top = need.right = need.bottom = need.left = ring;
        }
      }
      var sh = cs.boxShadow;
      if (sh && sh !== 'none') {
        /* split on commas that are not inside a colour function */
        var parts = [], depth = 0, cur = '';
        for (var c = 0; c < sh.length; c++) {
          var ch = sh[c];
          if (ch === '(') depth++;
          if (ch === ')') depth--;
          if (ch === ',' && depth === 0) { parts.push(cur); cur = ''; continue; }
          cur += ch;
        }
        parts.push(cur);
        for (var q = 0; q < parts.length; q++) {
          var part = parts[q];
          if (/\binset\b/.test(part)) continue;
          var nums = (part.match(/-?[\d.]+px/g) || []).map(parseFloat);
          if (nums.length < 2) continue;
          var ox = nums[0], oy = nums[1];
          var blur = nums.length > 2 ? nums[2] : 0;
          var spread = nums.length > 3 ? nums[3] : 0;
          var reach = blur / 2 + spread;
          need.right = Math.max(need.right, ox + reach);
          need.left = Math.max(need.left, -ox + reach);
          need.bottom = Math.max(need.bottom, oy + reach);
          need.top = Math.max(need.top, -oy + reach);
        }
      }
      need.top = Math.max(0, Math.ceil(need.top));
      need.right = Math.max(0, Math.ceil(need.right));
      need.bottom = Math.max(0, Math.ceil(need.bottom));
      need.left = Math.max(0, Math.ceil(need.left));
      return need;
    },
    /* The box in DOCUMENT coordinates, which is what a page screenshot clips
       against: getBoundingClientRect is viewport-relative and the two only agree
       while the page has not scrolled.
       THE AIR AROUND IT IS MEASURED, NOT CHOSEN. A fixed 12px pad is right for a
       button in a row 14px from its neighbour and wrong for one in a sheet body
       whose gap is 8, and the picture then shows half of the control below as if
       it were part of this one. So each side is padded to at most HALF the
       distance to the nearest thing that is not this element's own ancestor or
       descendant: the picture keeps the ground it stands on and never borrows a
       neighbour.
       AND THAT HALVING USED TO WIN AGAINST THE SUBJECT ITSELF, which is the
       defect this second argument closes. the specimen row set a 14px gap, so every
       facing side of every control in a specimen row was capped at 7px whatever
       the caller asked for, and 7px is EXACTLY the reach of the brass hover glow
       and 3px more than a focus ring needs: the worst case had zero margin and
       anything larger was cut. The crop was in the png, so no change to the page
       that displays it could put back a pixel that was never captured. want is
       what extentAt() says the element paints outside its box, and it is a
       FLOOR the neighbour rule may not go under. What is returned says whether
       that floor was met, so a frame that is still short is recorded rather than
       shipped as a confident picture of a cropped thing. */
    /* THE BOX OF THE FIRST VISIBLE MATCH OF A SELECTOR, in document coordinates
       and with a flat pad. Not boxAt, and the difference is the whole point:
       boxAt derives its pad from the distance to the nearest neighbour, because
       it frames a PHOTOGRAPH and a photograph may not show part of the control
       next door. This frames a WINDOW onto the live specimen, where the
       neighbours are not a leak, they are context: a close button with the
       corner of its own sheet behind it reads better than a close button in a
       void. So the pad is a flat number and the neighbours stay.
       No backtick in this block on purpose: everything here is injected into
       the page as a template literal, and one backtick ends it. That is what
       took the first cut of this function down before it ran once.
       Used by crops.cjs for the census on ui-kit/button.html. */
    boxOf: function (sel, pad) {
      var all;
      try { all = document.querySelectorAll(sel); } catch (e) { return null; }
      pad = pad == null ? 10 : pad;
      for (var i = 0; i < all.length; i++) {
        var el = all[i], r = el.getBoundingClientRect();
        if (!r.width || !r.height || inert(el)) continue;
        /* A WINDOW MAY NOT ASK FOR PIXELS THE DOCUMENT DOES NOT HAVE. The
           account dropdown in the header specimen is 196 wide and starts at
           x=1012 in a document 1120 wide, so 88px of it are painted past the
           viewport and are simply not there: the census window asked for
           1002..1218 and the reader got a box that was half menu and half
           nothing. Clamped, the window is the part that exists, which for a
           left-aligned menu is the labels. The clipped field records how much
           was asked for and not given, so a window showing less than the whole
           control is a number rather than a surprise. (No backtick anywhere in
           this block: it is injected as a template literal, and one backtick
           ends it.) */
        var docW = document.documentElement.clientWidth;
        var docH = Math.max(document.documentElement.scrollHeight, document.body.scrollHeight);
        var x = Math.max(0, Math.round(r.left + (window.scrollX || 0) - pad));
        var y = Math.max(0, Math.round(r.top + (window.scrollY || 0) - pad));
        var w = Math.round(r.width + pad * 2), h = Math.round(r.height + pad * 2);
        var clipped = Math.max(0, (x + w) - docW) + Math.max(0, (y + h) - docH);
        return { x: x, y: y, w: Math.min(w, Math.max(1, docW - x)),
                 h: Math.min(h, Math.max(1, docH - y)),
                 clipped: clipped, matches: all.length };
      }
      return null;
    },
    boxAt: function (i, pad, want) {
      var el = document.querySelector('[data-paint="' + i + '"]');
      if (!el) return null;
      var r = el.getBoundingClientRect();
      pad = pad || 0;
      want = want || { top: 0, right: 0, bottom: 0, left: 0 };
      var gap = { top: pad, right: pad, bottom: pad, left: pad };
      var all = document.body.getElementsByTagName('*');
      for (var n = 0; n < all.length; n++) {
        var o = all[n];
        if (o === el || el.contains(o) || o.contains(el)) continue;
        var b = o.getBoundingClientRect();
        if (!b.width || !b.height) continue;
        var overV = b.bottom > r.top && b.top < r.bottom;
        var overH = b.right > r.left && b.left < r.right;
        if (overV && b.right <= r.left) gap.left = Math.min(gap.left, (r.left - b.right) / 2);
        if (overV && b.left >= r.right) gap.right = Math.min(gap.right, (b.left - r.right) / 2);
        if (overH && b.bottom <= r.top) gap.top = Math.min(gap.top, (r.top - b.bottom) / 2);
        if (overH && b.top >= r.bottom) gap.bottom = Math.min(gap.bottom, (b.top - r.bottom) / 2);
      }
      /* the subject's own reach is a floor the neighbour rule may not go under */
      gap.top = Math.max(gap.top, want.top);
      gap.right = Math.max(gap.right, want.right);
      gap.bottom = Math.max(gap.bottom, want.bottom);
      gap.left = Math.max(gap.left, want.left);
      var l = Math.max(0, Math.floor(gap.left)), t = Math.max(0, Math.floor(gap.top));
      var x = r.left + window.scrollX - l, y = r.top + window.scrollY - t;
      /* CLAMPING THE ORIGIN WITHOUT CLAMPING THE SIZE MOVES THE PICTURE. An
         element 12px from the top of the document takes x/y = 0 and kept its
         full padded height, so the frame slid DOWN by the amount it was clamped
         and took a slice of the row below with it. Measured on the quiet
         .auth-btn, whose picture carried the top of the brass one under it. */
      if (x < 0) { l += x; x = 0; }
      if (y < 0) { t += y; y = 0; }
      var rgt = Math.max(0, Math.floor(gap.right));
      var bot = Math.max(0, Math.floor(gap.bottom));
      /* THE FAR EDGES CLAMP FOR THE SAME REASON THE NEAR ONES DO. A frame that
         runs past the last pixel of the document is not a small picture, it is
         an error out of the screenshot API and it takes the whole run with it,
         which is how this was found: a bet sheet is position:fixed, so it is
         painted in the VIEWPORT and is not part of the document's scroll extent
         at all, and the moment the pad stopped being a flat 12 the frame reached
         past the end of the image. The clip is intersected with the document, in
         both origin and size, and got is written from what survived, so a
         short side is reported rather than crashed on. */
      var docW = document.documentElement.scrollWidth;
      var docH = document.documentElement.scrollHeight;
      var over = (r.left + window.scrollX + r.width + rgt) - docW;
      if (over > 0) rgt = Math.max(0, rgt - over);
      over = (r.top + window.scrollY + r.height + bot) - docH;
      if (over > 0) bot = Math.max(0, bot - over);
      var got = { top: Math.max(0, t), right: rgt,
                  bottom: bot, left: Math.max(0, l) };
      /* WHAT THE FRAME DID NOT MANAGE TO HOLD. Zero on every picture in a healthy
         tree; non-zero says the document itself has the subject nearer an edge
         than its own paint reaches, which is a fact about the specimen and has to
         be visible rather than absorbed. */
      var short = Math.max(0, want.top - got.top, want.right - got.right,
                           want.bottom - got.bottom, want.left - got.left);
      var w = Math.ceil(r.width + got.left + got.right);
      var h = Math.ceil(r.height + got.top + got.bottom);
      /* the subject itself may be outside the image: a fixed element on a short
         page. A frame that cannot be taken is reported as not taken, never as a
         picture of something else, which is lesson 6 in a third place. */
      if (x >= docW || y >= docH) return null;
      w = Math.min(w, docW - x);
      h = Math.min(h, docH - y);
      if (w <= 0 || h <= 0) return null;
      return { x: x, y: y, width: w, height: h,
               want: want, got: got, short: short };
    },
    /* DISABLED IS READ AND NEVER SET. Setting the attribute to take the picture
       would be the stand class this whole section exists to avoid: it would
       prove the rule renders, not that any screen ships it. All three spellings,
       because button.css answers all three. */
    disabledAt: function (i) {
      var el = document.querySelector('[data-paint="' + i + '"]');
      if (!el) return false;
      return el.disabled === true || el.hasAttribute('disabled') ||
             el.getAttribute('aria-disabled') === 'true';
    },
    focusedIs: function (i) {
      return document.activeElement === document.querySelector('[data-paint="' + i + '"]');
    },
    /* every class in the document, so a caller can work out which component
       files decide what this document looks like. getAttribute and not
       className: on an SVG element className is an SVGAnimatedString and
       stringifies to [object SVGAnimatedString]. */
    allClasses: function () {
      var out = {}, all = document.querySelectorAll('[class]');
      for (var i = 0; i < all.length; i++) {
        var v = all[i].getAttribute('class') || '';
        v.split(/\\s+/).forEach(function (c) { if (c) out[c] = 1; });
      }
      return Object.keys(out).sort();
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
    /* 11, and the reason it exists at all: a PICTURE of a state, raised the way
       a person raises it. rest is no interaction, hover is the pointer, active
       is the pointer with the button held, focus is a real Tab walk until the
       element is the active one. Nothing sets a class and nothing sets an
       attribute; a state this document cannot reach comes back null and is
       reported as not staged rather than staged by the instrument.
       Returns the five values the picture was taken at, so the manifest can say
       what the image shows and a reader is never asked to trust a png. */
    async shoot(i, state, file) {
      const el = await page.$('[data-paint="' + i + '"]');
      if (!el) return null;
      await page.mouse.move(1, 1);
      try { await el.scrollIntoViewIfNeeded({ timeout: 2000 }); } catch (e) { return null; }
      /* A FIXED ELEMENT IS PAINTED IN THE VIEWPORT AND NOT IN THE DOCUMENT, so
         `getBoundingClientRect().top + scrollY` is its document coordinate only
         while the page is AT the top. The bet sheet is a real bottom drawer and
         the specimen keeps it fixed on purpose; the moment the specimen page
         gained enough padding to scroll at all, that sum ran past the end of the
         page image and the screenshot API took the whole run down with it. The
         page is put back to the top for those, which is where the drawer's own
         coordinates are true. */
      const fixed = await page.evaluate((n) => {
        var e = document.querySelector('[data-paint="' + n + '"]');
        while (e && e !== document.body) {
          if (getComputedStyle(e).position === 'fixed') return true;
          e = e.parentElement;
        }
        return false;
      }, i);
      if (fixed) await page.evaluate(() => window.scrollTo(0, 0));
      if (state === 'hover' || state === 'active') {
        try { await el.hover({ timeout: 2000 }); } catch (e) { return null; }
        if (state === 'active') await page.mouse.down();
      } else if (state === 'focus') {
        await page.evaluate(() => {
          document.body.setAttribute('tabindex', '-1');
          document.body.focus();
        });
        let on = false;
        for (let n = 0; n < 80 && !on; n++) {
          await page.keyboard.press('Tab');
          on = await page.evaluate('__ask.focusedIs(' + i + ')');
        }
        if (!on) return null;
      }
      const ms = await page.evaluate('__ask.settleMs()');
      await page.waitForTimeout(Math.max(ms, 60) + 60);
      /* AND THEN ASK THE ELEMENT WHETHER IT HAS ACTUALLY STOPPED. settleMs()
         reads the longest transition DECLARED in the stylesheets, which is the
         right number for a document and not always for an element: it does not
         know about a delay on this rule, an animation on an ancestor, or a
         compositor that started late. Measured: the confirm button of the win
         overlay came back at
             rgba(199, 162, 78, 0.98) 0px 5.88701px 17.661px -7.84935px
         where the settled value is
             rgb(199, 162, 78) 0px 6px 18px -8px
         and 98 per cent of a glow is a DIFFERENT FACE as far as a signature
         comparison is concerned. It became a sixth gallery on the button page
         whose entire content was that a shadow had not finished arriving.
         So the wait above is a floor and this is the check: read the face, read
         it again, and stop when two consecutive reads agree. A face that is
         still moving is not a face. 12 x 50ms is the ceiling, and reaching it
         means the element genuinely never settles, which is worth knowing and
         is not silently waited out.

         AND THE READING IS KEPT, rather than the face being read again at the
         end. It used to be taken after the screenshot, and a `fullPage`
         screenshot is not a passive observer: Chromium scrolls the page to
         assemble it, the element travels out from under the pointer and back,
         `:hover` drops and re-applies, and the read that followed caught a
         160ms transition about 3ms from its start. That is where
         `rgba(199, 162, 78, 0.98)` came from, and no amount of waiting BEFORE
         the screenshot could have fixed it, because the thing that disturbed
         the element happened after the wait. The picture and the value are now
         taken of the same settled state, which is the only order in which the
         value can be said to describe the picture. */
      let last = await page.evaluate('__ask.paintAt(' + i + ')');
      for (let n = 0; n < 12; n++) {
        await page.waitForTimeout(50);
        const now = await page.evaluate('__ask.paintAt(' + i + ')');
        if (now === last) break;
        last = now;
      }
      /* THE PAD IS DERIVED FROM THE SUBJECT, IN THE STATE IT IS IN. Asked after
         the state is raised and not before, because the thing that leaves the box
         is usually the state itself: at rest a quiet button paints nothing outside
         its edge, and on hover it carries a brass glow. 12 stays as a minimum so a
         control with no reach at all still gets air around it. */
      const want = await page.evaluate('__ask.extentAt(' + i + ')');
      const clip = await page.evaluate(
        '__ask.boxAt(' + i + ', 12, ' + JSON.stringify(want || {}) + ')');
      let value = null;
      if (clip && clip.width && clip.height) {
        /* TWO PIXELS PER CSS PIXEL FOR A CONTROL, ONE FOR A PANEL. A hover on a
           36px button is a 1px edge and a 4-step colour move, and at 1x that is
           a smudge; a card is 440px wide and its state reads perfectly at 1x.
           Shooting everything at 2x made the card component alone 15.5MB of a
           19MB folder, for pictures nobody would look closer at. The threshold
           is the width at which a thing stops being a control. */
        /* fullPage IS WHAT MAKES THE CLIP DOCUMENT-RELATIVE, and without it the
           two coordinate systems agreed only by luck. boxAt() has always
           returned DOCUMENT coordinates; a clip without fullPage is measured
           against the VIEWPORT image, and every specimen page used to be short
           enough never to scroll, so document and viewport were the same
           numbers. The first specimen tall enough to scroll - which is what
           giving the page a 12px edge to be photographed in did - put an element
           at document y 962 on a 900px viewport and the API refused the whole
           run. Proved both ways before it was changed: the same clip fails
           without fullPage at scroll 0 and at scroll 138, and succeeds with it
           at both. */
        /* A NULL PATH MEASURES AND DOES NOT WRITE, AND THAT IS THE COMMON CASE.
           The clip is computed either way, so every value below - the settled
           face, the box, the pad that was wanted against the pad that was got -
           is the same whether or not a png comes out of it, and the gates that
           read them do not change. What changes is that this pass stopped
           writing 718 files nothing renders: `_gen_component_pages.py` puts a
           picture on a page only for `disabled`, the one state a reader cannot
           raise on the live specimen three sections up, and the capture had
           never followed that decision. ui-kit/docs/backlog.md S42. */
        if (file) {
          await page.screenshot({
            path: file, fullPage: true,
            clip: { x: clip.x, y: clip.y, width: clip.width, height: clip.height },
            scale: clip.width > 360 ? 'css' : 'device' });
        }
        value = { value: last, w: Math.round(clip.width), h: Math.round(clip.height),
                  pad: clip.got, needed: clip.want, short: clip.short };
      }
      if (state === 'active') await page.mouse.up();
      if (state === 'focus') await page.evaluate(() => document.activeElement.blur());
      await page.mouse.move(1, 1);
      return value;
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

/* The shortest window a pinned box has to fit inside, for lesson 9. Same reason
   as floorFor: one number, not one per script.
   640 is the 1366x768 laptop, still the commonest small desktop screen, with
   about 120px of browser chrome taken off it. Chosen as a floor and not as a
   target: everything in this product that is pinned to the top of a window
   should fit a screen that ordinary, and anything that does not has to say so
   out loud. */
const SHORTEST_VIEWPORT = 640;

module.exports = { PROBE, open, browser, shutdown, floorFor, SHORTEST_VIEWPORT };
