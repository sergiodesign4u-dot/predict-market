/* ui-kit/_verify/audit.cjs - ask a browser the four questions, on any set of pages.

   This is the check that used to be rewritten every step: contrast, links with
   no rule behind them, horizontal overflow, dead icon references, requests that
   404, a pinned box taller than the window it is pinned to, and the focus ring
   at every tab stop. It asks browser.cjs, so the instrument lessons are applied
   once rather than remembered ten times.

       python3 -m http.server 8901          # from the repo root, in another shell

       node ui-kit/_verify/audit.cjs ui-kit/why.html ui-kit/patterns.html
       node ui-kit/_verify/audit.cjs --kit           # every vitrine page
       node ui-kit/_verify/audit.cjs --screens       # every painted screen
       node ui-kit/_verify/audit.cjs --kit --focus   # and every tab stop

   Options: --port N (default 8901), --widths 360,1440, --themes dark,light,
   --focus (walk the tab order and measure each ring), --json.

   The pinned-box question runs as a second pass in a window of its own, at
   browser.cjs SHORTEST_VIEWPORT. There is no flag for that height: a check for
   a defect only visible in a short window is not a check if the window can be
   made tall.

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
    // kit.html and specimens.extra.html are SOURCES, not pages: the first is
    // frozen provenance and the second is a bag of blocks the extractor cuts
    // specimens out of, which renders as fragments with no .app-case around
    // them. Auditing either measures a file nobody visits.
    const SOURCE = new Set(['kit.html', 'specimens.extra.html']);
    for (const f of fs.readdirSync(path.join(ROOT, 'ui-kit')).sort()) {
      if (f.endsWith('.html') && !SOURCE.has(f)) out.push('ui-kit/' + f);
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
  let measured = 0, tabs = 0, blind = 0, pins = 0, unpainted = 0;

  for (const theme of THEMES) {
    for (const width of WIDTHS) {
      const s = await B.open({ width });
      for (const rel of targets) {
        await s.go(`http://127.0.0.1:${PORT}/${rel}`, theme);
        const where = `${rel} ${theme}@${width}`;

        const all = await s.ask('contrast()');
        // A blended or filtered element is UNMEASURABLE from `color`, not
        // failing: the pixel is decided after the cascade. An element whose ink
        // is transparent or whose face is 0px paints no glyph at all, so it has
        // no contrast to measure either. Both are counted apart so the number of
        // things nobody measured is visible instead of implied.
        blind += all.filter((e) => e.blended).length;
        unpainted += all.filter((e) => !e.blended && e.unpainted).length;
        const low = all.filter((e) => !e.blended && !e.unpainted &&
                                      e.ratio < B.floorFor(e.size, e.weight));
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

  /* Lesson 9, and it is its own pass because it needs its own WINDOW. Every
     other question here is about a pixel and is answered at any height; this one
     is about whether a person can reach the pixel, and it is only visible in a
     short window. Themes are not walked: a colour cannot move a box, so the
     geometry is the same in both and running it twice would only cost time. */
  const short = { height: B.SHORTEST_VIEWPORT };
  for (const width of WIDTHS) {
    const s = await B.open({ width, height: short.height });
    for (const rel of targets) {
      await s.go(`http://127.0.0.1:${PORT}/${rel}`, THEMES[0]);
      for (const p of await s.ask('pinned()')) {
        pins += 1;
        if (p.needs > p.vh && !p.scrolls) {
          findings.push(`${rel} @${width}x${p.vh}: ${p.el} is ${p.position} at ` +
            `${p.anchor}:${p.offset}px and ${p.height}px tall, so ${p.needs - p.vh}px of it ` +
            `is off the window and it has no scroll of its own`);
        }
      }
    }
    await s.close();
  }
  await B.shutdown();

  const head = `${targets.length} page(s), ${THEMES.length} theme(s), ${WIDTHS.length} width(s)` +
    ` = ${measured} render(s)` + (has('focus') ? `, ${tabs} tab stop(s)` : '') +
    `, ${pins} pinned box(es) at ${B.SHORTEST_VIEWPORT}px of window` +
    (blind ? `, ${blind} unmeasurable (blend or filter)` : '') +
    (unpainted ? `, ${unpainted} painting no glyph (transparent ink or 0px face)` : '');
  if (has('json')) {
    console.log(JSON.stringify({ head, findings }, null, 1));
  } else {
    console.log(head);
    console.log(findings.length ? findings.join('\n') : 'clean: 0 findings');
  }
  process.exit(findings.length ? 1 : 0);
})();
