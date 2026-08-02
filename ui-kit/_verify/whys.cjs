/* For a list of (page, selector, property, width), report which css rule wins
   before the swap and which wins after, so a difference can be traced to the
   rule that caused it rather than guessed at.
*/
const fs = require('fs');
const { execSync } = require('child_process');
// One reader of the browser, and this script needs its cache rule as much as
// the pixel ones: the question it answers is "which rule wins", and a stale
// stylesheet answers it with yesterday's cascade. That is not hypothetical, it
// is how a .tc-page move first measured as a defect.
const B = require('./browser.cjs');

const ROOT = require('path').resolve(__dirname, '..', '..');
const CASES = [
  ['event-feed-crypto.html', '.subcat', 'position', 380],
  ['event-feed-crypto.html', '.cat-layout', 'align-items', 380],
  ['event-feed-crypto.html', '.subcat ul', 'flex-direction', 380],
  ['event-feed-crypto.html', '.thumb', 'background-color', 1280],
  ['event-feed-crypto.html', '.subcat button', 'justify-content', 1280],
  ['event-feed-crypto.html', '.subcat button', 'border-top-width', 1280],
  ['active-bets.html', '.pos', 'background-color', 1280],
  ['active-bets.html', '.pos-side', 'padding-left', 1280],
  ['toasts.html', '.toast', 'background-color', 1280],
  ['wallet.html', '.cta-bar', 'background-color', 1280],
  ['cookie-consent.html', '.cc-banner', 'background-color', 1280],
  ['event-detail-bet-error.html', '.confirm-btn', 'background-color', 380],
  ['event-detail-logged-out-multi.html', '.fine', 'color', 1280],
];

const probe = async (page, sel, prop) => page.evaluate(([sel, prop]) => {
  const el = document.querySelector(sel);
  if (!el) return { error: 'no element' };
  const hits = [];
  const walk = (rules, from, media) => {
    for (const r of rules) {
      if (r.styleSheet) {
        let sub; try { sub = r.styleSheet.cssRules; } catch (e) { continue; }
        walk(sub, (r.href || from).split('/').slice(-1)[0], media);
      } else if (r.cssRules && r.conditionText !== undefined) {
        const ok = window.matchMedia(r.conditionText).matches;
        if (ok) walk(r.cssRules, from, `@${r.conditionText}`);
      } else if (r.selectorText && r.style && r.style.getPropertyValue(prop)) {
        for (const one of r.selectorText.split(',')) {
          let m = false; try { m = el.matches(one.trim()); } catch (e) { m = false; }
          if (m) hits.push(`${from}${media ? ' ' + media : ''}  {${one.trim()}}  ${r.style.getPropertyValue(prop)}${r.style.getPropertyPriority(prop) ? ' !' : ''}`);
        }
      }
    }
  };
  for (const sheet of document.styleSheets) {
    let rules; try { rules = sheet.cssRules; } catch (e) { continue; }
    walk(rules, (sheet.href || 'inline').split('/').slice(-1)[0], '');
  }
  return { computed: getComputedStyle(el)[prop.replace(/-(\w)/g, (m, c) => c.toUpperCase())], hits };
}, [sel, prop]);

(async () => {

  for (const [name, sel, prop, width] of CASES) {
    const tmp = `_old-${name}`;
    fs.writeFileSync(`${ROOT}/ui-visual/${tmp}`,
      execSync(`git show HEAD:ui-visual/${name}`, { cwd: ROOT, maxBuffer: 1 << 28 }));
    const s = await B.open({ width });
    const page = s.page;
    console.log(`\n===== ${name}  ${sel}  ${prop}  @${width}`);
    for (const [file, tag] of [[tmp, 'OLD'], [name, 'NEW']]) {
      await page.goto(`http://localhost:8901/ui-visual/${file}`, { waitUntil: 'load' });
      const r = await probe(page, sel, prop);
      console.log(` ${tag} computed=${r.computed || r.error}`);
      (r.hits || []).forEach((h) => console.log(`      ${h}`));
    }
    await s.close();
    fs.unlinkSync(`${ROOT}/ui-visual/${tmp}`);
  }
  await B.shutdown();
})();
