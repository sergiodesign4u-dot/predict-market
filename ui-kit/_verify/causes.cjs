/* Group the differences by root cause instead of by page.

   A box that moved is usually a consequence: one element grew and everything
   below it shifted. What is worth reading is the set of PROPERTY changes, keyed
   by the element that carries them, because that is what a css rule did.

   usage: node causes.cjs <beforeDir> <afterDir>
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
// colour of a border that is 0px wide paints nothing; the browser reports it
// anyway because it inherits from `color`.
const BORDER_COLOR = new Set(['borderTopColor', 'borderBottomColor', 'borderLeftColor', 'borderRightColor']);


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

const read = (f) => JSON.parse(zlib.gunzipSync(fs.readFileSync(f)));
const [before, after] = [process.argv[2], process.argv[3]];
const files = fs.readdirSync(before).filter((f) => f.endsWith('.json.gz')).sort();

const causes = new Map();   // key -> {n, pages:Set}
for (const f of files) {
  const A = read(path.join(before, f)), B = read(path.join(after, f));
  const n = Math.min(A.length, B.length);
  for (let i = 0; i < n; i++) {
    const a = A[i], b = B[i];
    if (!a[6] && !b[6]) continue;
    const who = `${a[0]}${a[1] ? '.' + a[1].split(/\s+/).slice(0, 3).join('.') : ''}`;
    if (a[6] !== b[6]) {
      const k = `${who} :: VISIBLE ${a[6]} -> ${b[6]}`;
      if (!causes.has(k)) causes.set(k, { n: 0, pages: new Set() });
      causes.get(k).n++; causes.get(k).pages.add(f);
    }
    for (let k2 = 0; k2 < PROPS.length; k2++) {
      if (a[8][k2] === b[8][k2]) continue;
      const w = PROPS[k2];
      if (!paints(w, a, b)) continue;
      const key = `${who} :: ${w}: ${String(a[8][k2]).slice(0, 44)} -> ${String(b[8][k2]).slice(0, 44)}`;
      if (!causes.has(key)) causes.set(key, { n: 0, pages: new Set() });
      causes.get(key).n++; causes.get(key).pages.add(f);
    }
  }
}

const rows = [...causes.entries()].sort((x, y) => y[1].n - x[1].n);
console.log(`${rows.length} distinct property changes\n`);
for (const [k, v] of rows) {
  console.log(`${String(v.n).padStart(6)}x  ${v.pages.size.toString().padStart(3)} snaps  ${k}`);
}
