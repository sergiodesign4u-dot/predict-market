# Wireframes - Conventions (Step 02)

This is the wireframe rulebook for Predict Market. Every screen and every state
page built in Steps 03 to 08 follows these rules. Wireframes are grey-box, low
fidelity, structure only: layout and content order are the deliverable, not
visuals.

---

## The 7 base conventions

### 1. Fidelity: structure only

Show structure, hierarchy, and zones. Grey box. No color, no fonts, no brand,
no images, no finished UI. The layout and the order of content on the page are
what we are designing here. If a decision is about how something looks rather
than where it sits and what it says, it does not belong in a wireframe. The
grey-box layout is now responsive: structure and zones reflow across
breakpoints (see convention 7), while still grey with no color, fonts, icons,
or shadows.

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
- For invoked screens (Bet Screen, Sign In / Register, Deposit, Win Screen,
  Loss Screen), the base and state pages render as modal or bottom-sheet
  overlay content, not as a full-page layout. Their states are still separate
  pages, exactly as above.

### 6. Deferred to later phases (Concept onward), not allowed in wireframes

Not part of the wireframe deliverable and not to appear on any wireframe page:
color, typography, shadows, icons, finished UI, motion. These belong to the
Concept phase and later, never here.

### 7. Responsive build (mobile-first)

The product is responsive and built mobile-first. The mobile layout is the
base; desktop is a min-width expansion of the same screen. Wireframes build one
responsive screen, not a separate desktop mock.

**Mobile-to-desktop mapping** (from `IA/sitemap.md`, Desktop layer section,
restated here so a builder does not need to cross-read):

- **Navigation:** bottom nav with 4 slots on mobile becomes a horizontal top
  nav with the same 4 destinations on desktop, plus a right-hand utility
  cluster (Wallet, How It Works, avatar). No destination added or removed.
- **Notifications badge:** on the Notifications item, in the bottom nav on
  mobile, in the top nav on desktop. Always visible on both.
- **Event Feed:** single column on mobile, a responsive card grid up to 4 per
  row on desktop. The per-card context snippet is never dropped to fit more
  columns (snippet hard-lock, minimum card width around 280px).
- **Invoked screens** (Bet Screen, Sign In / Register, Deposit, Win Screen,
  Loss Screen): presented as an overlay in context on both breakpoints, a
  centered modal on desktop, a full-height bottom sheet on mobile. They are
  never a separate full-page destination and never a nav slot.

**Breakpoint thresholds** (set here, since `IA/sitemap.md` left the exact
pixels as a conventions detail):

- mobile, base: 1 column, bottom nav.
- min-width 640px: 2-column feed grid, and navigation switches from bottom nav
  to top nav at this first desktop breakpoint.
- min-width 960px: 3-column feed grid.
- min-width 1280px: 4-column feed grid.

Each threshold is the width where one more ~280px card column fits with gaps
without crowding out the context snippet. These are the feed-grid thresholds;
other screens reflow at the same mobile-first base but do not need a column
count.

This stays grey-box: the layout reflows across breakpoints, but everything is
still grey, with no color, fonts, icons, or shadows.

---

## Three additions (Predict Market needs these beyond the base 7)

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
