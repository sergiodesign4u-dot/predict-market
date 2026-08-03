/* ui-kit/_verify/states.cjs - photograph every state of a component, for real.

   WHY IT EXISTS. A stand page showed its states as a table of SELECTOR against
   WHAT MOVES, and `background:var(--bg-control-hover)` tells a person nothing
   about what a hover looks like. The reason it was a table and not a picture was
   a rule that is still right: a state faked with a stand class describes the
   stand instead of the product. The wrong conclusion was drawn from it. The
   answer to "do not fake it" is not "do not show it", it is SHOW THE REAL ONE,
   and browser.cjs already knows how to raise every state a person can: lesson 11
   is a real pointer, lesson 3 is a real Tab, a press is the mouse button held
   down, and disabled is an attribute the markup either carries or does not.

   WHAT A GROUP IS, and this is the part that is computed rather than judged.
   One class can be several pictures: `.provider-btn` is a row in the deposit
   dialog, a centred plate in the sign-in sheet and a quiet chip in the bet
   panel, because three scopes paint it differently. So every element carrying a
   state-bearing class is read at REST first and grouped by what it actually
   looks like - the five values that make a control's face - and each distinct
   face gets its own set of pictures. Two elements that measure identical are one
   picture, however many screens they stand on. Nobody picks the sample.

   WHAT IT WRITES.
     ui-kit/_states/<component>/<group>-<state>-<theme>.png
     ui-kit/_states/index.json    the manifest: every picture, the classes that
                                  were in its specimen, and the sources whose
                                  bytes decide it

   FRESHNESS IS NOT A PIXEL COMPARISON. The manifest records which files the
   picture was taken from; `ui-kit/_states.py` hashes those files and fails when
   the hash moves. A picture cannot be compared to a re-render without a browser
   in the build, and a browser in the build is a checker that needs a machine.
   Bytes are deterministic and a stale picture is exactly "one of my sources
   changed".

       node ui-kit/_verify/states.cjs            every component that has a plan
       node ui-kit/_verify/states.cjs button     one component

   No em dash.
*/
const fs = require('fs');
const path = require('path');
const B = require('./browser.cjs');

const ROOT = path.resolve(__dirname, '..', '..');
const KIT = path.join(ROOT, 'ui-kit');
const OUT = path.join(KIT, '_states');
const PORT = process.env.SNAP_PORT || '8901';

/* The states a browser can be asked for, and how each is raised. Nothing here
   sets a class: every one is the real mechanism a person would use.
     rest      no interaction at all
     hover     a real pointer on the middle of the box (lesson 11)
     active    the same pointer with the button held down
     focus     a real Tab walk until the element is the active one (lesson 3)
     disabled  read, never set: the markup carries the attribute or it does not */
const STATES = ['rest', 'hover', 'active', 'focus'];

/* The five values that make a control's FACE. Two elements that agree on all
   five are one picture. Chosen rather than "every property" on purpose: a
   different padding is the same face at a different size, and splitting on it
   would put the same picture on the page twice. */
const FACE = (cs) => [cs.backgroundColor, cs.backgroundImage, cs.borderTopColor,
                      cs.borderTopWidth, cs.color, cs.borderTopLeftRadius].join('|');

/* EVERY SPECIMEN THAT CARRIES THE CLASS, not the ones registered to the
   component. The first cut asked the manifest - `component === x` or x in
   `also` - and found two faces of the button, because .provider-btn and
   .confirm-btn stand inside specimens that belong to dialog, betpanel and
   outcome-dialog, and neither lists button in `also`. Those two classes are 574
   of the family's 704 uses. A corpus drawn from the registry answers "what does
   the registry say", and the question here is "where does this class actually
   stand". The html is read first so only the documents that can contain
   something are opened. */
function specimensFor(component, manifest, classes) {
  const has = (id) => {
    const f = path.join(KIT, 'specimens', id + '.html');
    if (!fs.existsSync(f)) return false;
    const src = fs.readFileSync(f, 'utf8');
    return classes.some((c) => new RegExp(`class="[^"]*\\b${c}\\b`).test(src));
  };
  const own = (s) => s.component === component || (s.also || []).includes(component);
  // canonical specimens first, so a face found in two documents is filed under
  // the component's own page rather than under whichever was read first
  return [...manifest.filter((s) => own(s) && has(s.id)),
          ...manifest.filter((s) => !own(s) && has(s.id))];
}

/* THE SUBJECT OF EVERY STATE RULE, which is a SELECTOR and not a class name.
   The first cut took the last class name out of the selector and searched for
   that, and it was wrong in both directions at once.
   `.app-case .state-btn:not(.primary):hover` splits before the pseudo into
   `.app-case .state-btn:not(.primary)`, whose last class name is `primary`, so
   the quiet button was never searched for and the brass one was found by
   accident. `.app-case .cta-bar button:hover` has no class on its subject at
   all, so the name that came out was `cta-bar` and what got photographed was the
   BAR: a 700px plate standing in for a button.
   The subject is the whole head of the selector. It is handed to the browser as
   written, so the scope that decides the paint comes with it, and the grouping
   by rest face collapses the ones that overlap. */
/* A STATE INSIDE :not() IS NOT THIS RULE'S STATE, and splitting on the bare
   token cut a selector in half mid-parenthesis: cookie-consent writes
   `input[type="checkbox"]:not(:disabled)`, the split produced
   `input[type="checkbox"]:not(` and the browser threw on an invalid selector,
   which killed the whole run seven components in. Depth is tracked, and only a
   token at depth zero ends the head. */
function headOf(sel) {
  const STATE = /^(:hover|:active|:focus-visible|:focus|:disabled|\[aria-disabled)/;
  let depth = 0;
  for (let i = 0; i < sel.length; i++) {
    const ch = sel[i];
    if (ch === '(' || ch === '[') depth++;
    else if (ch === ')' || ch === ']') depth--;
    if (depth === 0 && STATE.test(sel.slice(i))) return sel.slice(0, i).trim();
  }
  return null;
}

function stateSubjects(component) {
  const css = fs.readFileSync(path.join(ROOT, 'components', component + '.css'), 'utf8')
    .replace(/\/\*[\s\S]*?\*\//g, ' ');
  const out = new Set();
  const STATE = /:hover|:active|:focus-visible|:focus|:disabled|\[aria-disabled/;
  for (const m of css.matchAll(/([^{}]+)\{/g)) {
    const sel = m[1].trim();
    if (sel.startsWith('@') || !STATE.test(sel)) continue;
    // a comma inside :is(...) or :not(...) does not separate two selectors
    let depth = 0, part = '';
    const parts = [];
    for (const ch of sel) {
      if (ch === '(' || ch === '[') depth++;
      else if (ch === ')' || ch === ']') depth--;
      if (ch === ',' && depth === 0) { parts.push(part); part = ''; } else part += ch;
    }
    parts.push(part);
    for (const one of parts) {
      const head = headOf(one.trim());
      if (head) out.add(head);
    }
  }
  return [...out];
}

/* Which class names to grep the specimen html for, so only documents that can
   contain a subject are opened. Scope classes are not dropped: `.cta-bar` is
   how a document that holds a bare-button subject is recognised. */
function classesIn(subjects) {
  const out = new Set();
  for (const s of subjects) {
    for (const m of s.matchAll(/\.([\w-]+)/g)) if (m[1] !== 'app-case') out.add(m[1]);
  }
  return [...out];
}

(async () => {
  const manifest = JSON.parse(fs.readFileSync(path.join(KIT, 'specimens', 'index.json'), 'utf8'));
  const want = process.argv.slice(2).filter((a) => !a.startsWith('--'));
  const components = want.length ? want
    : [...new Set(manifest.map((s) => s.component))].sort();

  fs.mkdirSync(OUT, { recursive: true });
  const rows = [];

  for (const component of components) {
    /* A SPECIMEN'S `component` IS NOT ALWAYS A STYLESHEET. The registry files
       one specimen under `icons`, which is a sprite sheet and has no
       components/icons.css to read state rules out of, and the run died on it
       after twenty-nine components with every picture taken and no manifest
       written. A corpus taken from one registry has to be filtered by the other.*/
    if (!fs.existsSync(path.join(ROOT, 'components', component + '.css'))) {
      console.log(`${component}: no stylesheet of its own, skipped`);
      continue;
    }
    const subjects = stateSubjects(component);
    if (!subjects.length) { console.log(`${component}: no state rule, nothing to photograph`); continue; }
    const classes = classesIn(subjects);
    const specs = specimensFor(component, manifest, classes);
    const dir = path.join(OUT, component);
    fs.mkdirSync(dir, { recursive: true });
    const seen = new Map();          // dark face -> group record
    const owner = new Map();         // "specimen|index" -> group, decided in dark

    /* THE GROUPING IS DECIDED IN ONE THEME AND ONLY ONE. The first cut keyed on
       the rest face in whichever theme was being walked, and a face in daylight
       is a different string from the same face on graphite, so every control
       came out twice: 11 groups where there are 6, half of them holding only
       dark pictures and half only light. The face is read on graphite, the
       element is remembered by its position in ITS OWN document, which is stable
       across loads, and the daylight pass photographs the same elements rather
       than rediscovering them. A theme is a value, never an identity. */
    for (const theme of ['dark', 'light']) {
      for (const spec of specs) {
        const s = await B.open({ width: Math.max(spec.width || 900, 420), height: 900, scale: 2 });
        await s.go(`http://127.0.0.1:${PORT}/ui-kit/specimens/${spec.id}.html`, theme);
        const found = await s.ask(`paint(${JSON.stringify(subjects.join(','))})`);
        // every class in this document, so the freshness hash can name the
        // component files whose bytes decide this picture
        const inDoc = await s.ask('allClasses()');

        for (const el of found) {
          const at = `${spec.id}|${el.i}`;
          let group;
          if (theme === 'dark') {
            const key = `${el.el}|${el.rest}`;
            group = seen.get(key);
            if (!group) {
              group = { id: `g${seen.size + 1}`, el: el.el, scope: el.scope,
                        specimen: spec.id, classes: inDoc, shots: {} };
              seen.set(key, group);
            } else if (group.specimen !== spec.id) {
              // the same face in a second specimen is the same picture; record
              // the extra home so the page can say where else it stands
              group.also = [...new Set([...(group.also || []), spec.id])];
              continue;
            } else {
              continue;             // a second copy of a face already shot here
            }
            owner.set(at, group);
          } else {
            group = owner.get(at);
            if (!group || group.specimen !== spec.id) continue;
          }

          for (const state of STATES) {
            const file = `${group.id}-${state}-${theme}.png`;
            const shot = await s.shoot(el.i, state, path.join(dir, file));
            if (!shot) continue;
            group.shots[`${state}-${theme}`] = { file: `${component}/${file}`, ...shot };
          }
          // disabled is read and never set
          const dis = await s.ask(`disabledAt(${el.i})`);
          if (dis) {
            const file = `${group.id}-disabled-${theme}.png`;
            const shot = await s.shoot(el.i, 'rest', path.join(dir, file));
            if (shot) group.shots[`disabled-${theme}`] = { file: `${component}/${file}`, ...shot };
          }
        }
        await s.close();
      }
    }
    for (const g of seen.values()) rows.push({ component, ...g });
    console.log(`${component}: ${seen.size} distinct face(s), ` +
                `${[...seen.values()].reduce((n, g) => n + Object.keys(g.shots).length, 0)} picture(s)`);
  }
  await B.shutdown();

  const prev = fs.existsSync(path.join(OUT, 'index.json'))
    ? JSON.parse(fs.readFileSync(path.join(OUT, 'index.json'), 'utf8')) : [];
  const kept = prev.filter((r) => !components.includes(r.component));
  fs.writeFileSync(path.join(OUT, 'index.json'),
                   JSON.stringify([...kept, ...rows].sort((a, b) =>
                     (a.component + a.id).localeCompare(b.component + b.id)), null, 1) + '\n');
  console.log(`manifest: ${kept.length + rows.length} group(s)`);
  console.log('now run: python3 ui-kit/_states.py --stamp');
})();
