/* One element, shot from the old head and the new head, side by side.
   usage: node side.cjs <page.html> <selector> <outName> [width]
   Writes <outName>-old.jpg and <outName>-new.jpg into the scratchpad. */
const fs = require('fs');
const { execSync } = require('child_process');
// Two versions of one element, so the two shots MUST be taken in the same
// regime. browser.cjs is the only thing here that opens a browser, for exactly
// that reason.
const B = require('./browser.cjs');

const ROOT = require('path').resolve(__dirname, '..', '..');
const SCRATCH = process.env.OUT_DIR || require('os').tmpdir();
const [pageName, selector, outName, widthArg] = process.argv.slice(2);
const width = Number(widthArg || 1280);
const TMP = `_old-${pageName}`;

(async () => {
  // the pre-swap copy of the same page, served from the same folder so every
  // relative path still resolves
  fs.writeFileSync(`${ROOT}/ui-visual/${TMP}`,
    execSync(`git show HEAD:ui-visual/${pageName}`, { cwd: ROOT, maxBuffer: 1 << 28 }));
  const s = await B.open({ width });
  const page = s.page;
  for (const [file, tag] of [[TMP, 'old'], [pageName, 'new']]) {
    await page.goto(`http://localhost:8901/ui-visual/${file}`, { waitUntil: 'load' });
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(150);
    const el = await page.$(selector);
    if (!el) { console.log(`${tag}: no ${selector}`); continue; }
    await el.screenshot({ path: `${SCRATCH}/${outName}-${tag}.jpg`, type: 'jpeg', quality: 92 });
    console.log(`${SCRATCH}/${outName}-${tag}.jpg`);
  }
  await s.close();
  await B.shutdown();
  fs.unlinkSync(`${ROOT}/ui-visual/${TMP}`);
})();
