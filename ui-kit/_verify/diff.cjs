/* Diff two snapshot directories, element by element and property by property.

   usage: node diff.cjs <beforeDir> <afterDir> [--full] [--top N]
*/
const fs = require('fs');
const path = require('path');
const zlib = require('zlib');

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


// A property that changed is only a difference if something draws with it. A
// colour on an element with no text of its own is inherited by children that
// set their own; a border colour under a 0px border draws no line.
const IDX = {};
PROPS.forEach((p, i) => { IDX[p] = i; });
function paints(prop, a, b) {
  if (prop === 'color') return a[7] === 1 || b[7] === 1;
  if (prop.startsWith('border') && prop.endsWith('Color')) {
    const w = IDX[prop.replace('Color', 'Width')];
    return a[8][w] !== '0px' || b[8][w] !== '0px';
  }
  return true;
}

/* A HOST AND A PORT ARE NOT A DIFFERENCE. Two trees can only be compared by
   serving them at once, which means two ports, and every `url()` a page resolves
   then carries the port it was served from: 700 background images reported as
   changed on a pass that changed no image. Normalised here rather than at the
   call site, because a caller that has to remember to normalise is a caller that
   will one day forget and read 700 as a finding. */
const SAME_ORIGIN = /https?:\/\/(?:localhost|127\.0\.0\.1|\[::1\]):\d+/g;
const unport = (v) => typeof v === 'string' && v.indexOf('://') > -1
  ? v.replace(SAME_ORIGIN, 'http://SERVED') : v;
const read = (f) => JSON.parse(zlib.gunzipSync(fs.readFileSync(f)));
const before = process.argv[2], after = process.argv[3];
const full = process.argv.includes('--full');
const shown = full ? 1e9 : 10;

const files = fs.readdirSync(before).filter((f) => f.endsWith('.json.gz')).sort();
let pagesChanged = 0, elsChanged = 0;
const byProp = new Map();
const report = [];

for (const f of files) {
  const ap = path.join(after, f);
  if (!fs.existsSync(ap)) { report.push(`${f}: MISSING after`); pagesChanged++; continue; }
  const A = read(path.join(before, f)), B = read(ap);
  const lines = [];
  if (A.length !== B.length) lines.push(`  element count ${A.length} -> ${B.length}`);
  const n = Math.min(A.length, B.length);
  let count = 0;
  for (let i = 0; i < n; i++) {
    const a = A[i], b = B[i];
    const parts = [];
    // Invisible on both sides: nothing it holds can be seen, so nothing it
    // holds can be a regression. The grey-box scaffolding lives here.
    if (!a[6] && !b[6]) continue;
    if (a[6] !== b[6]) {
      parts.push(`VISIBILITY ${a[6] ? 'shown' : 'hidden'} -> ${b[6] ? 'shown' : 'hidden'}`);
      byProp.set('visible', (byProp.get('visible') || 0) + 1);
    }
    if (a[2] !== b[2] || a[3] !== b[3] || a[4] !== b[4] || a[5] !== b[5]) {
      parts.push(`box [${a[2]},${a[3]} ${a[4]}x${a[5]}] -> [${b[2]},${b[3]} ${b[4]}x${b[5]}]`);
      byProp.set('box', (byProp.get('box') || 0) + 1);
    }
    for (let k = 0; k < PROPS.length; k++) {
      const av = unport(a[8][k]), bv = unport(b[8][k]);
      if (av !== bv && paints(PROPS[k], a, b)) {
        parts.push(`${PROPS[k]}: ${String(a[8][k]).slice(0, 60)} -> ${String(b[8][k]).slice(0, 60)}`);
        byProp.set(PROPS[k], (byProp.get(PROPS[k]) || 0) + 1);
      }
    }
    if (!parts.length) continue;
    count++;
    if (count <= shown) {
      const who = `${a[0]}${a[1] ? '.' + a[1].split(/\s+/).join('.') : ''}`;
      lines.push(`  #${i} ${who.slice(0, 64)}\n      ${parts.join('\n      ')}`);
    }
  }
  if (count > shown) lines.push(`  ... and ${count - shown} more elements on this page`);
  if (lines.length) { pagesChanged++; elsChanged += count; report.push(`\n${f}\n${lines.join('\n')}`); }
}

console.log(report.join('\n'));
console.log(`\n${files.length} snapshots compared, ${pagesChanged} differ, ${elsChanged} elements changed`);
if (byProp.size) {
  console.log('\nby property:');
  [...byProp.entries()].sort((x, y) => y[1] - x[1])
    .forEach(([k, v]) => console.log(`  ${String(v).padStart(6)}  ${k}`));
}
