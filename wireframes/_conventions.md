# Wireframes - Conventions (Step 02)

This is the wireframe rulebook for Predict Market. Every screen and every state
page built in Steps 03 to 08 follows these rules. Wireframes are grey-box, low
fidelity, structure only: layout and content order are the deliverable, not
visuals.

---

## The 6 base conventions

### 1. Fidelity: structure only

Show structure, hierarchy, and zones. Grey box. No color, no fonts, no brand,
no images, no finished UI. The layout and the order of content on the page are
what we are designing here. If a decision is about how something looks rather
than where it sits and what it says, it does not belong in a wireframe.

### 2. Markup: semantic HTML

Build with semantic elements: `header`, `nav`, `main`, `section`, `article`,
`form`, `button`, `label`, `ul`/`li`. Not a wall of `div`. Each screen must
read as a real document outline, so the heading and landmark structure alone
tells you what the screen is.

### 3. Text: real domain text, never lorem ipsum

Every label and string is real Predict Market content, pulled from
`IA/sitemap.md` where the phrasing already exists. Examples of the exact
phrasings to reuse:

- Event questions in the form "Will X happen before [date]?"
- Categories: Politics, Crypto, Culture, General.
- The price-context narrative (why this price, key arguments for YES and NO):
  our FJ2 differentiator.
- Resolution conditions (what counts as YES, what source is authoritative).
- The fee line: "platform earns $X if you win".
- The funds-protection line: "Your USDC is held 1:1 - we do not lend or invest
  deposited funds."
- The plain-language resolution note on the Loss screen (what resolved and why).

Never lorem ipsum. If a real string exists in the sitemap, use it verbatim.

### 4. File names: base page per screen, one page per state

Pattern only (the actual list is produced in Step 03):

- Base page per screen: `wireframes/<screen>.html`
- One page per state: `wireframes/<screen>-<state>.html`
- Lower kebab-case. The `<state>` suffix matches the state name exactly as
  written in `wireframes/_screens.md` (for example `-empty`, `-error`,
  `-loading`, `-reconcile`, `-insufficient-balance`, `-resolved`, `-pending`).

Do not enumerate the file list here. That is Step 03's job.

### 5. States: every state is a separate page

Each state is its own page, never a toggle or a variant inside one file. Same
structure, different content.

- The base page is the success or representative state.
- Each additional real state from `_screens.md` gets its own page: the
  canonical states (`-empty`, `-error`, `-loading`) and the product-specific
  states (such as `-reconcile`, `-insufficient-balance`, `-resolved`,
  `-pending`).
- Every real state listed for a screen in `_screens.md` must become its own
  page when that screen is built. Nothing listed there is dropped or merged.

### 6. Deferred to later phases (Concept onward), not allowed in wireframes

Not part of the wireframe deliverable and not to appear on any wireframe page:
color, typography, shadows, icons, finished UI, motion. These belong to the
Concept phase and later, never here.

---

## Three additions (Predict Market needs these beyond the base 6)

### A. Grey-box rule for data

Predict Market screens carry data the generic demo product does not: a
probability chart, the % number, fees, payouts, and USDC amounts. The grey-box
rule still holds, with two clarifications:

- A chart is a labeled placeholder zone, for example a bordered box captioned
  "probability chart". Never a drawn, plotted, or faked chart.
- The % number and money amounts are real, labeled sample values (for example
  "67%", "$5", "$8.50 potential payout"), never lorem and never an empty box.
  A number that carries meaning is shown as a number, because the layout cannot
  be judged without it.

### B. Sample-content honesty

Example events, names, and amounts in the wireframes are illustrative sample
data. They are realistic so the layout reads true, but they are not a real
market and not a finding from research.

- Realistic domain content is allowed as a sample.
- It is never labeled or implied to be a real event or a verified fact.

This keeps the "never invent" rule intact while the screens stay legible: the
content looks like the product, but no page claims a sample event is real.

### C. Annotations and on-page navigation tree

Per the Phase B roadmap, every wireframe ties back to the research. Two required
page elements:

- **Light annotations.** Each major block on a screen carries a short note
  linking it to the job or research finding it serves (for example "context
  narrative -> FJ2 differentiator", "fee line -> H6"). Keep annotations out of
  the layout flow: put them in a side note or a footnote list, so the grey box
  stays clean and the annotations do not get mistaken for UI.
- **On-page navigation tree.** Each wireframe page shows a short tree of where
  this screen sits among the others (the main-flow spine from `_screens.md`:
  Event Feed -> Event Detail -> Bet Screen -> Sign In / Register -> Deposit ->
  Active Bets), so any single page is readable in context. This is a required
  element of every page. It is described here, not built here.

---

## Two scope notes

### Bet Screen base page is the intent state

The Bet Screen base page (`wireframes/bet-screen.html`) is the intent state, the
representative view of the screen. Its success is the transition into Active
Bets, so the Bet Screen does NOT get a separate `-success` page. Every other
spine screen uses success as its base page, per Rule 5.

### Every product-specific state stays its own page

Keeping every product-specific state as its own page is deliberate. For the Bet
Screen this means several pages (intent as the base, then `-reconcile`,
`-insufficient-balance`, `-event-closed`, `-error`). Each one resolves a
distinct moment of the money flow, so none is dropped or collapsed. Recording
this here so the page count is expected, not a surprise, in Step 03.

---

## What comes next

The per-screen file list and the screens themselves are produced from Step 03
onward, with each later step reading this file before building anything.
