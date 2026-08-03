/* Snapshot every painted screen: for each element, where it sits and what it is
   painted with. Run once before the CSS swap and once after, then diff.

   A screenshot proves "it looks the same" only as well as the eye reading it.
   This measures it: 45 computed properties and the element box, per element, per
   viewport. If one padding moves by a pixel the diff names the element and the
   property.

   usage: node snap.cjs <outDir> [pageName ...]
*/
const fs = require('fs');
const path = require('path');
const zlib = require('zlib');
// The browser is opened by browser.cjs and never here. Every session it hands
// back is a FRESH CONTEXT WITH THE CACHE OFF, which is the rule this script
// broke: it reused one context per viewport, so a -before run against a warm
// cache and an -after run against a cold one measured nine screens 7,500 to
// 11,200 pixels apart, and every one of them collapsed to 0 when both batches
// were shot in the same regime.
const B = require('./browser.cjs');

const ROOT = require('path').resolve(__dirname, '..', '..');
// Which tree to walk. It used to be ui-visual only, and that is how step 7b
// broke the vitrine without noticing: `.sidebar-divider` is built at run time by
// _nav.js, so deleting the rule left every group heading in the kit's side panel
// as unstyled text, and no snapshot covered the page it happened on. A pass that
// edits components/ has to be able to prove BOTH trees.
//     node snap.cjs <outDir>                 the painted product
//     node snap.cjs <outDir> --kit           the vitrine and its specimens
const KIT_MODE = process.argv.includes('--kit');
const BASE = 'http://localhost:' + (process.env.SNAP_PORT || '8901') + '/';
const TREE = KIT_MODE ? 'ui-kit/' : 'ui-visual/';
// One width inside every band the system has a breakpoint for (640, 860, 900,
// 1440), so a rule that escaped its media query cannot hide between two of them.
const VIEWPORTS = [
  ['mobile', 380, 820],
  ['tablet', 700, 900],
  ['dock', 880, 900],
  ['desktop', 1280, 900],
  ['wide', 1500, 900],
];

const PROPS = [
  'display', 'position', 'visibility', 'opacity', 'zIndex', 'transform',
  'color', 'backgroundColor', 'backgroundImage', 'backgroundSize', 'backgroundPosition',
  'borderTopWidth', 'borderRightWidth', 'borderBottomWidth', 'borderLeftWidth',
  'borderTopStyle', 'borderTopColor', 'borderBottomColor', 'borderLeftColor', 'borderRightColor',
  'borderTopLeftRadius', 'borderTopRightRadius', 'borderBottomLeftRadius', 'borderBottomRightRadius',
  'boxShadow', 'fontFamily', 'fontSize', 'fontWeight', 'fontStyle', 'lineHeight',
  'letterSpacing', 'textTransform', 'textAlign', 'textDecorationLine', 'whiteSpace',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'marginTop', 'marginRight', 'marginBottom', 'marginLeft',
  'rowGap', 'columnGap', 'flexDirection', 'flexWrap', 'alignItems', 'justifyContent',
  'gridTemplateColumns', 'overflowX', 'overflowY', 'fill', 'stroke', 'strokeWidth',
];

async function snapshot(page) {
  return await page.evaluate((props) => {
    // Elements that paint nothing and whose count changes with the swap (the
    // inline <style> is what is being removed) would shift every index after
    // them and make the whole page read as different. They are not measured.
    const SKIP = {HEAD: 1, TITLE: 1, META: 1, LINK: 1, STYLE: 1, SCRIPT: 1, BASE: 1};
    const all = [...document.querySelectorAll('*')].filter((e) => !SKIP[e.tagName]);
    // A SCROLL POSITION IS NOT A STYLESHEET PROPERTY, so it is normalised away
    // before anything is measured. Both side panels in this repo scroll their
    // current entry into view on load, and where that lands is a race with the
    // webfont: the same page under the SAME stylesheet put the course rail at
    // scrollTop 2246 and 2247 on consecutive loads, and the vitrine's panel at
    // 1585 in one run of this script and 1601 in the next. Every element inside
    // a rail then reads as moved, which is 990 phantom differences in the
    // painted tree and 9,773 in the vitrine, all of them noise with a real
    // regression free to hide inside. The boxes below are recorded relative to
    // the document, so zeroing every scroller costs nothing and buys a diff
    // whose floor is zero.
    window.scrollTo(0, 0);
    for (const el of all) if (el.scrollTop || el.scrollLeft) { el.scrollTop = 0; el.scrollLeft = 0; }
    const out = [];
    for (let i = 0; i < all.length; i++) {
      const el = all[i];
      const r = el.getBoundingClientRect();
      const cs = getComputedStyle(el);
      const vals = props.map((p) => cs[p]);
      // Whether the element paints at all. The grey-box scaffolding is
      // display:none in both cascades, so its colours may differ freely.
      // Does this element paint text itself? A colour on a wrapper whose children
      // all set their own is a value nothing draws with.
      let txt = 0;
      for (const n of el.childNodes) {
        if (n.nodeType === 3 && n.nodeValue.trim()) { txt = 1; break; }
      }
      const vis = el.checkVisibility
        ? el.checkVisibility({ opacityProperty: true, visibilityProperty: true, contentVisibilityAuto: true })
        : cs.display !== 'none';
      out.push([
        el.tagName.toLowerCase(),
        (el.getAttribute('class') || '').trim().slice(0, 80),
        Math.round(r.x), Math.round(r.y + window.scrollY),
        Math.round(r.width), Math.round(r.height),
        vis ? 1 : 0,
        txt,
        vals,
      ]);
    }
    return out;
  }, PROPS);
}

(async () => {
  const outDir = process.argv[2];
  let pages = process.argv.slice(3).filter((a) => !a.startsWith('--'));
  if (!pages.length && KIT_MODE) {
    pages = fs.readdirSync(path.join(ROOT, 'ui-kit'))
      .filter((f) => f.endsWith('.html') && f !== 'selftest.html').sort()
      .concat(fs.readdirSync(path.join(ROOT, 'ui-kit', 'specimens'))
        .filter((f) => f.endsWith('.html')).sort().map((f) => 'specimens/' + f));
  } else if (!pages.length) {
    pages = fs.readdirSync(path.join(ROOT, 'ui-visual'))
      .filter((f) => f.endsWith('.html') && f !== 'overview.html').sort();
  }
  fs.mkdirSync(outDir, { recursive: true });

  for (const [vp, w, h] of VIEWPORTS) {
    const s = await B.open({ width: w, height: h });
    const page = s.page;
    for (const name of pages) {
      await page.goto(BASE + TREE + name, { waitUntil: 'load' });
      await page.evaluate(() => document.fonts.ready);
      // Freeze anything that moves, in both runs alike, so a shimmer never
      // reads as a difference.
      //
      // PAUSED IS NOT FROZEN, and that took a whole sweep to see. This line used
      // to only pause, and a pause happens wherever the animation has got to:
      // ui-visual/win.html slides its dialog in, and four identical loads put it
      // at y=120.9, 133.1, 149.2 and 159.6. Every element inside a sliding box
      // then reads as moved, so a diff of two runs of the SAME stylesheet
      // reported 25 differing snapshots and 1,745 changed boxes, which is a
      // noise floor high enough to hide a real regression inside it.
      // finish() is the fixed point: every animation and transition is put at
      // its END state, which is the state the screen settles into and the only
      // one two runs can agree on. An infinite animation cannot finish, so it
      // keeps the pause, and the style tag below still catches anything that
      // starts after this line.
      await page.evaluate(() => {
        document.getAnimations().forEach((a) => {
          try { a.finish(); } catch (e) { a.pause(); }
        });
      });
      await page.addStyleTag({ content: '*,*::before,*::after{animation-play-state:paused!important}' });
      await page.waitForTimeout(120);
      const snap = await snapshot(page);
      fs.writeFileSync(path.join(outDir, `${name.replace('/', '-')}.${vp}.json.gz`),
        zlib.gzipSync(JSON.stringify(snap)));
      process.stdout.write('.');
    }
    await s.close();
    process.stdout.write(` ${vp} done\n`);
  }
  await B.shutdown();
})();
