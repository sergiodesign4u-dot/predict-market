/* Compare two snapshots by what PAINTS, not by index.

   diff.cjs walks the two element lists in step, which is right when the DOM is
   fixed and only the styling moves. It is wrong the moment a pass removes
   markup: every index after the removal points at a different element and the
   whole page reads as changed.

   This one keeps only the elements the browser reports as visible and compares
   those sequences. Removing something display:none cannot change what paints,
   so if the pass was honest the two sequences match element for element. If a
   removal moved a sibling, changed a :last-child, or renumbered an :nth-child,
   it shows up here as a real difference on a real element.

   usage: node visible.cjs <beforeDir> <afterDir>
*/
const fs = require('fs');
const path = require('path');
const zlib = require('zlib');

const PROPS = require('./snap-props.json');
const [A, B] = process.argv.slice(2);

const read = (d, f) => JSON.parse(zlib.gunzipSync(fs.readFileSync(path.join(d, f))));
const files = fs.readdirSync(A).filter((f) => f.endsWith('.json.gz'));

let pages = 0, differ = 0, changed = 0, shape = 0;
const byProp = {};
for (const f of files) {
  if (!fs.existsSync(path.join(B, f))) continue;
  pages++;
  const a = read(A, f).filter((e) => e[6] === 1);
  const b = read(B, f).filter((e) => e[6] === 1);
  let bad = 0;
  if (a.length !== b.length) {
    shape++;
    console.log(f, 'visible element count', a.length, '->', b.length);
    continue;
  }
  for (let i = 0; i < a.length; i++) {
    const x = a[i], y = b[i];
    const lines = [];
    if (x[0] !== y[0] || x[1] !== y[1]) lines.push(`  identity ${x[0]}.${x[1]} -> ${y[0]}.${y[1]}`);
    for (let k = 2; k < 6; k++) if (x[k] !== y[k]) { lines.push(`  box [${x.slice(2, 6)}] -> [${y.slice(2, 6)}]`); break; }
    for (let p = 0; p < PROPS.length; p++) {
      if (x[8][p] !== y[8][p]) { lines.push(`  ${PROPS[p]}: ${x[8][p]} -> ${y[8][p]}`); byProp[PROPS[p]] = (byProp[PROPS[p]] || 0) + 1; }
    }
    if (lines.length) {
      bad++;
      if (changed < 60) console.log(`${f} #${i} ${y[0]}.${y[1]}\n` + lines.join('\n'));
      changed++;
    }
  }
  if (bad) differ++;
}
console.log(`\n${pages} snapshots, ${shape} with a different visible count, ${differ} differ, ${changed} visible elements changed`);
Object.entries(byProp).sort((a, b) => b[1] - a[1]).forEach(([k, v]) => console.log(String(v).padStart(6), k));
