/* One element, shot from the old head and the new head, side by side.
   usage: node side.cjs <page.html> <selector> <outName> [width]
   Writes <outName>-old.jpg and <outName>-new.jpg into the scratchpad. */
const fs = require('fs');
const { execSync } = require('child_process');
const { chromium } = require(process.env.PLAYWRIGHT_MODULE
  || '/Users/sergiyshevchenko/.npm/_npx/9833c18b2d85bc59/node_modules/playwright');

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
  const browser = await chromium.launch({ channel: 'chrome' });
  const ctx = await browser.newContext({ viewport: { width, height: 900 }, deviceScaleFactor: 1 });
  const page = await ctx.newPage();
  for (const [file, tag] of [[TMP, 'old'], [pageName, 'new']]) {
    await page.goto(`http://localhost:8901/ui-visual/${file}`, { waitUntil: 'load' });
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(150);
    const el = await page.$(selector);
    if (!el) { console.log(`${tag}: no ${selector}`); continue; }
    await el.screenshot({ path: `${SCRATCH}/${outName}-${tag}.jpg`, type: 'jpeg', quality: 92 });
    console.log(`${SCRATCH}/${outName}-${tag}.jpg`);
  }
  await browser.close();
  fs.unlinkSync(`${ROOT}/ui-visual/${TMP}`);
})();
