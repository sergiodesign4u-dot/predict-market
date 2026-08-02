/* ui-kit/_verify/audit.cjs - ask a browser the four questions, on any set of pages.

   This is the check that used to be rewritten every step: contrast, links with
   no rule behind them, horizontal overflow, dead icon references, requests that
   404, and the focus ring at every tab stop. It asks browser.cjs, so the six
   instrument lessons are applied once rather than remembered six times.

       python3 -m http.server 8901          # from the repo root, in another shell

       node ui-kit/_verify/audit.cjs ui-kit/why.html ui-kit/patterns.html
       node ui-kit/_verify/audit.cjs --kit           # every vitrine page
       node ui-kit/_verify/audit.cjs --screens       # every painted screen
       node ui-kit/_verify/audit.cjs --kit --focus   # and every tab stop

   Options: --port N (default 8901), --widths 360,1440, --themes dark,light,
   --focus (walk the tab order and measure each ring), --json.

   Exit code is 1 when anything failed, so it can gate a step by itself.
   No em dash.
*/
const fs = require('fs');
const path = require('path');
const B = require('./browser.cjs');

const ROOT = path.resolve(__dirname, '..', '..');
const argv = process.argv.slice(2);
const flag = (name, fallback) => {
  const i = argv.indexOf('--' + name);
  return i > -1 && argv[i + 1] && !argv[i + 1].startsWith('--') ? argv[i + 1] : fallback;
};
const has = (name) => argv.includes('--' + name);

const PORT = flag('port', '8901');
const WIDTHS = flag('widths', '360,1440').split(',').map(Number);
const THEMES = flag('themes', 'dark,light').split(',');
const MAX_TABS = 60;

function pages() {
  const named = argv.filter((a) => !a.startsWith('--') && a.endsWith('.html'));
  if (named.length) return named;
  const out = [];
  if (has('kit')) {
    for (const f of fs.readdirSync(path.join(ROOT, 'ui-kit')).sort()) {
      if (f.endsWith('.html') && f !== 'kit.html') out.push('ui-kit/' + f);
    }
  }
  if (has('screens')) {
    for (const f of fs.readdirSync(path.join(ROOT, 'ui-visual')).sort()) {
      if (f.endsWith('.html')) out.push('ui-visual/' + f);
    }
  }
  if (!out.length) {
    console.error('audit: name pages, or pass --kit / --screens');
    process.exit(2);
  }
  return out;
}

(async () => {
  const targets = pages();
  const findings = [];
  let measured = 0, tabs = 0;

  for (const theme of THEMES) {
    for (const width of WIDTHS) {
      const s = await B.open({ width });
      for (const rel of targets) {
        await s.go(`http://127.0.0.1:${PORT}/${rel}`, theme);
        const where = `${rel} ${theme}@${width}`;

        const low = (await s.ask('contrast()')).filter(
          (e) => e.ratio < B.floorFor(e.size, e.weight));
        measured += 1;
        for (const e of low.slice(0, 6)) {
          findings.push(`${where}: ${e.ratio}:1 on ${e.el} "${e.text}"`);
        }
        for (const a of await s.ask('uaLinks()')) {
          findings.push(`${where}: link with no rule, "${a.text}" (${a.el})`);
        }
        const ox = await s.ask('overflowX()');
        if (ox > 0) findings.push(`${where}: ${ox}px of horizontal overflow`);
        for (const d of await s.ask('deadIcons()')) {
          findings.push(`${where}: dead icon reference ${d}`);
        }

        if (has('focus')) {
          const seen = new Set();
          for (let i = 0; i < MAX_TABS; i++) {
            const r = await s.tab(1);
            if (!r || seen.has(r.el)) break;
            seen.add(r.el);
            tabs += 1;
            if (!r.visible) findings.push(`${where}: no ring on ${r.el}`);
            else if (r.ratio < 3) findings.push(`${where}: ring ${r.ratio}:1 on ${r.el}`);
          }
        }
      }
      for (const f of s.failed) findings.push(`${theme}@${width}: ${f.status} ${f.url}`);
      for (const e of s.errors) findings.push(`${theme}@${width}: console ${e.url} ${e.text}`);
      await s.close();
    }
  }
  await B.shutdown();

  const head = `${targets.length} page(s), ${THEMES.length} theme(s), ${WIDTHS.length} width(s)` +
    ` = ${measured} render(s)` + (has('focus') ? `, ${tabs} tab stop(s)` : '');
  if (has('json')) {
    console.log(JSON.stringify({ head, findings }, null, 1));
  } else {
    console.log(head);
    console.log(findings.length ? findings.join('\n') : 'clean: 0 findings');
  }
  process.exit(findings.length ? 1 : 0);
})();
